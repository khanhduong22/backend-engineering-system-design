# 🏆 GOF & ARCHITECTURAL DESIGN PATTERNS: HIGH-ROI STUDY GUIDE

> **Author:** Duong Phuc Khanh (Senior Fullstack & System Architect)  
> **Purpose:** Xếp hạng trọn bộ 23 GoF Design Patterns trong ĐÚNG 1 BẢNG DUY NHẤT + Chi tiết 16 Patterns hay gặp nhất (Tier 1, 2, 3) — Ưu tiên học các Pattern dùng nhiều nhất trong Backend/NestJS hàng ngày.

---

## 📊 1. BẢNG XẾP HẠNG THỐNG NHẤT TRỌN BỘ 23 GOF DESIGN PATTERNS (BY TIER)

| STT | Pattern Name | Tier / ROI | Nhóm GoF | Tần suất trong BE | Tác dụng & Use Case chính |
|---|---|---|---|---|---|
| 1 | **Strategy** | **Tier 1 (MUST)** | Behavioral | 🔥 Rất cao | Thay thế `if-else` / `switch-case` chật chội. Đổi thuật toán linh hoạt (Payment, Pricing). |
| 2 | **Factory Method** | **Tier 1 (MUST)** | Creational | 🔥 Rất cao | Tạo đối tượng động dựa vào tham số đầu vào (`type: 'EMAIL' | 'SMS'`). |
| 3 | **Observer / Pub-Sub** | **Tier 1 (MUST)** | Behavioral | 🔥 Rất cao | Phát Event bất đồng bộ (`UserRegistered` -> Gửi Noti, Tạo Ví, Index Search). |
| 4 | **Singleton** | **Tier 1 (MUST)** | Creational | 🔥 Rất cao | Đảm bảo 1 Instance duy nhất (DB Pool, Redis Client, NestJS `@Injectable()`). |
| 5 | **Decorator** | **Tier 1 (MUST)** | Structural | 🔥 Rất cao | Bọc thêm tính năng (NestJS `@UseGuards()`, Caching Wrapper bọc Repository). |
| 6 | **Adapter** | **Tier 1 (MUST)** | Structural | 🔥 Rất cao | Chuẩn hóa API 3rd-party (VNPay/Stripe payload) về DTO nội bộ của hệ thống. |
| 7 | **Chain of Responsibility**| **Tier 2 (HIGH)** | Behavioral | 🟡 Cao | Xây dựng Middleware Pipeline (Auth -> Role Check -> Rate Limit -> Handler). |
| 8 | **State** | **Tier 2 (HIGH)** | Behavioral | 🟡 Cao | Quản lý State Machine đơn hàng (`CREATED` -> `PAID` -> `SHIPPED` -> `CANCELLED`). |
| 9 | **Builder** | **Tier 2 (HIGH)** | Creational | 🟡 Cao | Dựng đối tượng phức tạp nhiều bước (SQL Query Builder, Test Data Fixtures). |
| 10 | **Proxy** | **Tier 2 (HIGH)** | Structural | 🟡 Cao | Control truy cập (Security Proxy, Lazy Loading, Nginx Reverse Proxy). |
| 11 | **Iterator** | **Tier 2 (HIGH)** | Behavioral | 🟡 Cao | Duyệt qua tập hợp dữ liệu (`for...of`, Async Generator functions). |
| 12 | **Abstract Factory** | **Tier 3 (NICHE)** | Creational | 🔵 Trung bình | Tạo họ các đối tượng liên quan (VD: Cross-platform DB Client Factory). |
| 13 | **Command** | **Tier 3 (NICHE)** | Behavioral | 🔵 Trung bình | Đóng gói Request thành Object (Undo/Redo, Queueing CLI commands). |
| 14 | **Template Method** | **Tier 3 (NICHE)** | Behavioral | 🔵 Trung bình | Định nghĩa khung thuật toán cố định ở Abstract Class cho class con override. |
| 15 | **Facade** | **Tier 3 (NICHE)** | Structural | 🔵 Trung bình | Gom nhiều subsystem phức tạp đằng sau 1 API interface đơn giản. |
| 16 | **Composite** | **Tier 3 (NICHE)** | Structural | 🔵 Trung bình | Quản lý cấu trúc cây đệ quy (File/Folder tree, Nested Menu multi-level). |
| 17 | **Prototype** | **Tier 4 (LOW)** | Creational | ⚪ Hiếm gặp | Clone đối tượng có sẵn (dùng `clone()` deep copy). |
| 18 | **Bridge** | **Tier 4 (LOW)** | Structural | ⚪ Hiếm gặp | Tách Abstraction khỏi Implementation (ít dùng trong BE hiện đại). |
| 19 | **Flyweight** | **Tier 4 (LOW)** | Structural | ⚪ Hiếm gặp | Chia sẻ bộ nhớ cho hàng ngàn đối tượng giống nhau (Game Engine). |
| 20 | **Mediator** | **Tier 4 (LOW)** | Behavioral | ⚪ Hiếm gặp | Trung gian giao tiếp giảm phụ thuộc chéo (Chat room server, Event Bus). |
| 21 | **Memento** | **Tier 4 (LOW)** | Behavioral | ⚪ Hiếm gặp | Lưu và khôi phục Snapshot trạng thái cũ của Object (Undo state). |
| 22 | **Visitor** | **Tier 4 (LOW)** | Behavioral | ⚪ Hiếm gặp | Thêm thuật toán mới vào class mà không sửa class đó (Compiler AST). |
| 23 | **Interpreter** | **Tier 4 (LOW)** | Behavioral | ⚪ Hiếm gặp | Xây dựng bộ đọc/dịch ngôn ngữ/cú pháp riêng (Regex, SQL Parser). |

---

## 🎯 2. CHI TIẾT TRỌN BỘ 16 PATTERNS HAY GẶP NHẤT (TIER 1, TIER 2, TIER 3)

---

### 🔥 TIÊN PHONG: NÓM TIER 1 (MUST-KNOW - HÀNG NGÀY)

#### 1. Strategy Pattern (Behavioral)
- **Vấn đề:** 10 cổng thanh toán (`VNPAY`, `MOMO`, `STRIPE`...). Dùng `if-else` làm file dài 1,000 dòng, vi phạm Open/Closed Principle.
- **Giải pháp:** Tạo interface `PaymentStrategy` và các class riêng cho từng cổng.
```typescript
interface PaymentStrategy { pay(amount: number): Promise<boolean>; }
class VnPayStrategy implements PaymentStrategy { async pay(amount: number) { return true; } }
class PaymentContext {
  constructor(private strategy: PaymentStrategy) {}
  execute(amount: number) { return this.strategy.pay(amount); }
}
```

#### 2. Factory Method Pattern (Creational)
- **Vấn đề:** Muốn khởi tạo đối tượng gửi notification (`EMAIL`, `SMS`, `PUSH`) mà không bắt Client dính chặt vào `new EmailProvider()`.
- **Giải pháp:** Dùng Factory class nhận `type` và tự đẻ ra Provider phù hợp.
```typescript
class NotificationFactory {
  static create(type: 'EMAIL' | 'SMS'): NotificationProvider {
    if (type === 'EMAIL') return new EmailProvider();
    return new SmsProvider();
  }
}
```

#### 3. Observer / Pub-Sub Pattern (Behavioral)
- **Vấn đề:** Đăng ký User xong phải Gửi Email + Tạo Ví 0đ + Index Search. Gọi đồng bộ sẽ làm request bị nghẽn 3 giây!
- **Giải pháp:** Phát Event `UserRegisteredEvent`. Các Observers tự động lắng nghe và chạy bất đồng bộ.
```typescript
eventEmitter.emit('user.registered', { userId: 123 });
eventEmitter.on('user.registered', async (data) => { await sendEmail(data.userId); });
```

#### 4. Singleton Pattern (Creational)
- **Vấn đề:** Mỗi request tạo 1 DB Connection Pool mới làm cạn kiệt RAM và sập Postgres Connection Limit!
- **Giải pháp:** Ép Class chỉ tồn tại **đúng 1 Instance duy nhất** trên toàn ứng dụng (Cơ chế `@Injectable()` mặc định của NestJS).
```typescript
class PrismaService {
  private static instance: PrismaService;
  static getInstance(): PrismaService {
    if (!this.instance) this.instance = new PrismaService();
    return this.instance;
  }
}
```

#### 5. Decorator Pattern (Structural)
- **Vấn đề:** Bổ sung Caching hay Auth Guard xung quanh 1 route/function mà không được sửa code gốc.
- **Giải pháp:** Bọc hàm gốc bên trong Decorator function (`@UseGuards()`, `@Get()`).
```typescript
function LogExecutionTime(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
  const originalMethod = descriptor.value;
  descriptor.value = async function (...args: any[]) {
    console.time(propertyKey);
    const result = await originalMethod.apply(this, args);
    console.timeEnd(propertyKey);
    return result;
  };
}
```

#### 6. Adapter Pattern (Structural)
- **Vấn đề:** VNPay trả về `{ vnp_ResponseCode: "00" }`, Stripe trả về `{ status: "succeeded" }`. Code bị hỗn loạn DTO.
- **Giải pháp:** Tạo Adapter ép tất cả dữ liệu bên thứ ba về đúng 1 DTO chuẩn nội bộ `{ success: boolean, txnId: string }`.
```typescript
class VnPayAdapter implements StandardPaymentResult {
  constructor(private raw: VnPayRawPayload) {}
  toStandard(): PaymentDTO {
    return { success: this.raw.vnp_ResponseCode === '00', txnId: this.raw.vnp_TxnRef };
  }
}
```

---

### 🟡 CHỦ LỰC: NHÓM TIER 2 (HIGH-VALUE - THƯỜNG XUYÊN)

#### 7. Chain of Responsibility Pattern (Behavioral)
- **Vấn đề:** Luồng kiểm tra Request trải qua nhiều bước: Validate Token ➔ Check Permission ➔ Rate Limit. Viết chung 1 hàm gây rối rắm.
- **Giải pháp:** Tách thành chuỗi các Handlers liên tiếp. Handler 1 xử lý xong chuyền sang Handler 2 (Chính là Middleware/Interceptor Pipeline).
```typescript
abstract class Handler {
  private next: Handler;
  setNext(next: Handler): Handler { this.next = next; return next; }
  async handle(req: any) { if (this.next) return this.next.handle(req); }
}
```

#### 8. State Pattern (Behavioral)
- **Vấn đề:** Đơn hàng có trạng thái `CREATED` ➔ `PAID` ➔ `SHIPPED` ➔ `CANCELLED`. Nếu dùng `if (status === 'CREATED')` ở mỗi hành động sẽ rất dễ đẻ ra bug chuyển trạng thái sai.
- **Giải pháp:** Mỗi trạng thái là 1 Class riêng tự quản lý hành vi hợp lệ của chính nó.
```typescript
interface OrderState { cancel(order: Order): void; pay(order: Order): void; }
class PaidState implements OrderState {
  cancel(order: Order) { throw new Error("Đơn đã thanh toán không thể hủy trực tiếp!"); }
  pay(order: Order) { /* No-op */ }
}
```

#### 9. Builder Pattern (Creational)
- **Vấn đề:** Khởi tạo 1 Object phức tạp có 20 tham số tùy chọn (VD: SQL Query hoặc Test Fixture). `new Query(a, b, null, null, c)` rất dễ truyền nhầm thứ tự!
- **Giải pháp:** Dùng Fluent API chaining để dựng đối tượng từng bước.
```typescript
const user = new UserBuilder().setName("Khanh").setAge(30).setRole("ADMIN").build();
```

#### 10. Proxy Pattern (Structural)
- **Vấn đề:** Kiểm soát truy cập (Access Control), Lazy Loading đối tượng nặng, hoặc đánh chặn phương thức (Interception) mà không cho Client biết.
- **Phân biệt với Decorator:** Decorator sinh ra để *thêm tính năng* (như Caching/Logging), còn Proxy sinh ra để *kiểm soát quyền truy cập / đại diện từ xa* (như JS `new Proxy()`, Protection Proxy, gRPC Remote Stub).
- **Giải pháp:** Tạo Proxy đóng vai trò "Kẻ gác cổng / Đại diện" chặn trước Object thật (Chính là cơ chế `ref() / reactive()` của Vue 3 hay ES6 `Proxy`).
```typescript
// ES6 Proxy API: Đánh chặn hành vi đọc/ghi Property của Object
const userAccount = { balance: 1000, role: 'USER' };

const securityProxy = new Proxy(userAccount, {
  get(target, prop) {
    console.log(`[AUDIT LOG] Ai đó vừa đọc trường: ${String(prop)}`);
    return target[prop];
  },
  set(target, prop, value) {
    if (prop === 'balance' && value < 0) {
      throw new Error("Số dư không thể là số âm!");
    }
    target[prop] = value;
    return true;
  }
});
```

#### 11. Iterator Pattern (Behavioral)
- **Vấn đề:** Muốn duyệt qua danh sách 1,000,000 records từ Database theo từng batch 100 items mà không kéo tràn bộ nhớ RAM.
- **Giải pháp:** Dùng Iterator / Async Generator để pull dữ liệu cuốn chiếu.
```typescript
async function* batchDbIterator(batchSize = 100) {
  let page = 0;
  while (true) {
    const items = await db.user.findMany({ skip: page * batchSize, take: batchSize });
    if (items.length === 0) break;
    yield items;
    page++;
  }
}
```

---

### 🔵 MỞ RỘNG: NHÓM TIER 3 (NICHE / RARE - BÀI TOÁN ĐẶC THÙ)

#### 12. Abstract Factory Pattern (Creational)
- **Vấn đề:** Cần khởi tạo nguyên một **Họ các đối tượng tương thích** (VD: Nếu là Database Postgres ➔ Tạo `PostgresConnection` + `PostgresQueryCompiler` + `PostgresGrammar`).
- **Giải pháp:** Tạo Factory của các Factory để đảm bảo không lắp nhầm `PostgresConnection` với `MySQLGrammar`.

#### 13. Command Pattern (Behavioral)
- **Vấn đề:** Đóng gói toàn bộ thông tin của 1 yêu cầu (hành động, tham số) thành 1 Object riêng biệt để lưu trữ vào Queue, hỗ trợ Undo/Redo hoặc Retry.
- **Giải pháp:** Tạo class `CreateOrderCommand` chứa dữ liệu và hàm `execute()`.

#### 14. Template Method Pattern (Behavioral)
- **Vấn đề:** Quy trình xuất Báo cáo có 4 bước: `FetchData()` ➔ `FormatData()` ➔ `GenerateFile()` ➔ `SendEmail()`. Bước 1 và 4 giống hệt nhau, chỉ có Bước 2 và 3 khác nhau giữa PDF và Excel.
- **Giải pháp:** Viết khung thuật toán ở Abstract Base Class, chừa hàm `FormatData()` cho class con override.

#### 15. Facade Pattern (Structural)
- **Vấn đề:** Đặt hàng phải gọi 5 dịch vụ: `InventoryService`, `PaymentService`, `ShippingService`, `EmailService`, `NotificationService`. Client gọi trực tiếp 5 dịch vụ này sẽ rất rối.
- **Giải pháp:** Tạo class `CheckoutFacade` bọc 5 dịch vụ lại, cấp đúng 1 hàm duy nhất: `checkoutFacade.placeOrder(cartId)`.

#### 16. Composite Pattern (Structural)
- **Vấn đề:** Quản lý danh mục sản phẩm hoặc Menu phân cấp nhiều tầng (Cấu trúc cây Tree đệ quy: Thư mục chứa File và Thư mục con).
- **Giải pháp:** Ép cả Node lá (File) và Node cha (Thư mục) dùng chung 1 interface `MenuComponent` để duyệt cây đệ quy đơn giản.

---

## 🚀 3. LỜI KHUYÊN HỌC ANKI DECK 01 HÔM NAY:
1. Master trọn vẹn **6 Pattern Tier 1** và **5 Pattern Tier 2**.
2. **Nguyên tắc "Code Replacement":** Khi lật thẻ Anki, luôn tự hỏi: *"Pattern này sinh ra để thay thế đoạn code xấu nào trong NestJS/TS?"*
3. **Các Pattern Tier 4 bỏ qua:** *Visitor, Interpreter, Flyweight, Memento, Bridge, Prototype* nằm trong phần khung máy/compiler, không tốn thời gian học thuộc!
