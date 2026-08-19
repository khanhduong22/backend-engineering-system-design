# 🏆 GOF & ARCHITECTURAL DESIGN PATTERNS: HIGH-ROI STUDY GUIDE

> **Author:** Duong Phuc Khanh (Senior Fullstack & System Architect)  
> **Purpose:** Xếp hạng trọn bộ 23 GoF Design Patterns theo tỷ lệ ROI (High Return on Investment) — Ưu tiên học các Pattern dùng nhiều nhất trong Backend/NestJS hàng ngày, loại bỏ việc nhồi nhét học thuộc lòng không thực tế.

---

## 📊 1. DANH SÁCH TRỌN BỘ 23 GOF DESIGN PATTERNS MATRIX

### A. Nhóm Creational Patterns (5 Patterns - Khởi tạo đối tượng)
| STT | Pattern Name | Tier / ROI | Tần suất trong BE | Tác dụng & Use Case chính |
|---|---|---|---|---|
| 1 | **Singleton** | **Tier 1 (MUST)** | 🔥 Rất cao | Đảm bảo 1 Instance duy nhất (DB Pool, Redis Client, NestJS `@Injectable()`). |
| 2 | **Factory Method** | **Tier 1 (MUST)** | 🔥 Rất cao | Tạo đối tượng động dựa vào tham số đầu vào (`type: 'EMAIL' | 'SMS'`). |
| 3 | **Abstract Factory** | **Tier 2 (HIGH)** | 🟡 Cao | Tạo họ các đối tượng liên quan (VD: UI Theme Factory, Cross-platform DB Factory). |
| 4 | **Builder** | **Tier 2 (HIGH)** | 🟡 Cao | Dựng đối tượng phức tạp nhiều bước (SQL Query Builder, Test Data Fixtures). |
| 5 | **Prototype** | **Tier 4 (LOW)** | ⚪ Hiếm gặp | Clone đối tượng có sẵn (dùng `clone()` deep copy). |

---

### B. Nhóm Structural Patterns (7 Patterns - Cấu trúc liên kết class)
| STT | Pattern Name | Tier / ROI | Tần suất trong BE | Tác dụng & Use Case chính |
|---|---|---|---|---|
| 6 | **Decorator** | **Tier 1 (MUST)** | 🔥 Rất cao | Bọc thêm tính năng (NestJS `@UseGuards()`, Caching Wrapper bọc Repository). |
| 7 | **Adapter** | **Tier 1 (MUST)** | 🔥 Rất cao | Chuẩn hóa API 3rd-party (VNPay/Stripe payload) về DTO nội bộ. |
| 8 | **Proxy** | **Tier 2 (HIGH)** | 🟡 Cao | Control truy cập (Security Proxy, Lazy Loading, Nginx Reverse Proxy). |
| 9 | **Facade** | **Tier 3 (NICHE)** | 🔵 Trung bình | Gom nhiều subsystem phức tạp đằng sau 1 API interface đơn giản. |
| 10 | **Composite** | **Tier 3 (NICHE)** | 🔵 Trung bình | Quản lý cấu trúc cây đệ quy (File/Folder tree, Nested Menu multi-level). |
| 11 | **Bridge** | **Tier 4 (LOW)** | ⚪ Hiếm gặp | Tách Abstraction khỏi Implementation (ít dùng trong BE hiện đại). |
| 12 | **Flyweight** | **Tier 4 (LOW)** | ⚪ Hiếm gặp | Chia sẻ bộ nhớ cho hàng ngàn đối tượng giống nhau (dùng trong Game/Graphics Engine). |

---

### C. Nhóm Behavioral Patterns (11 Patterns - Hành vi & Giao tiếp)
| STT | Pattern Name | Tier / ROI | Tần suất trong BE | Tác dụng & Use Case chính |
|---|---|---|---|---|
| 13 | **Strategy** | **Tier 1 (MUST)** | 🔥 Rất cao | Thay thế `if-else` / `switch-case` chật chội. Đổi thuật toán linh hoạt (Payment, Pricing). |
| 14 | **Observer / Pub-Sub** | **Tier 1 (MUST)** | 🔥 Rất cao | Phát Event bất đồng bộ (`UserRegistered` -> Gửi Noti, Tạo Ví, Index Search). |
| 15 | **Chain of Responsibility**| **Tier 2 (HIGH)** | 🟡 Cao | Middleware Pipeline (Auth -> Role Check -> Rate Limit -> Handler). |
| 16 | **State** | **Tier 2 (HIGH)** | 🟡 Cao | Quản lý State Machine đơn hàng (`CREATED` -> `PAID` -> `SHIPPED` -> `CANCELLED`). |
| 17 | **Iterator** | **Tier 2 (HIGH)** | 🟡 Cao | Duyệt qua tập hợp dữ liệu (`for...of`, Generator functions). |
| 18 | **Command** | **Tier 3 (NICHE)** | 🔵 Trung bình | Đóng gói Request thành Object (Undo/Redo, Queueing CLI commands). |
| 19 | **Template Method** | **Tier 3 (NICHE)** | 🔵 Trung bình | Định nghĩa khung thuật toán cố định ở Abstract Class cho class con override. |
| 20 | **Mediator** | **Tier 3 (NICHE)** | 🔵 Trung bình | Trung gian giao tiếp giảm phụ thuộc chéo (Chat room server, Event Bus). |
| 21 | **Memento** | **Tier 4 (LOW)** | ⚪ Hiếm gặp | Lưu và khôi phục Snapshot trạng thái cũ của Object (Undo state). |
| 22 | **Visitor** | **Tier 4 (LOW)** | ⚪ Hiếm gặp | Thêm thuật toán mới vào class mà không sửa class đó (dùng trong Compiler AST). |
| 23 | **Interpreter** | **Tier 4 (LOW)** | ⚪ Hiếm gặp | Xây dựng bộ đọc/dịch ngôn ngữ/cú pháp riêng (Regex, SQL Parser). |

---

## 🎯 2. CHI TIẾT CÁC PATTERN TIER 1 (CẦN NẮM NẰM LÒNG VÀO ANKI)

### 1. Strategy Pattern (Behavioral)
- **Vấn đề:** Có 10 phương thức thanh toán (`VNPAY`, `MOMO`, `PAYPAL`, `STRIPE`...). Nếu dùng `if-else` thì file code dài 1,000 dòng, mỗi lần thêm cổng mới phải sửa file cũ (Vi phạm nguyên lý SOLID - Open/Closed Principle).
- **Giải pháp:** Định nghĩa 1 Interface `PaymentStrategy` với hàm `pay(amount)`. Mỗi cổng thanh toán là 1 class triển khai interface đó.
- **Code NestJS/TS ngắn gọn:**
```typescript
interface PaymentStrategy {
  pay(amount: number): Promise<boolean>;
}

class VnPayStrategy implements PaymentStrategy {
  async pay(amount: number) { /* Gọi API VNPay */ return true; }
}

class PaymentContext {
  constructor(private strategy: PaymentStrategy) {}
  execute(amount: number) { return this.strategy.pay(amount); }
}
```

---

### 2. Factory Method Pattern (Creational)
- **Vấn đề:** Client không cần biết chi tiết khởi tạo một class phức tạp như nào, chỉ cần truyền vào tham số type (`'EMAIL'`, `'SMS'`, `'PUSH'`).
- **Giải pháp:** Tạo class Factory chứa hàm `createNotification(type)` trả về đúng Provider tương ứng.

---

### 3. Observer / Pub-Sub Pattern (Behavioral)
- **Vấn đề:** Khi hành động `UserRegistered` xảy ra, ta muốn gửi Email chào mừng, tạo Wallet 0đ, và đẩy data sang Analytics mà không làm nghẽn hàm đăng ký.
- **Giải pháp:** Publisher phát sự kiện `UserRegisteredEvent`. Các Observer (`EmailSubscriber`, `WalletSubscriber`) đăng ký lắng nghe và tự động chạy độc lập bất đồng bộ.

---

### 4. Adapter Pattern (Structural)
- **Vấn đề:** Cổng thanh toán VNPay trả về `{ vnp_ResponseCode: "00", vnp_TxnRef: "123" }`, trong khi Stripe trả về `{ status: "succeeded", id: "ch_123" }`.
- **Giải pháp:** Dùng Adapter chuyển đổi cả 2 định dạng khác nhau này về đúng 1 DTO chuẩn nội bộ: `{ success: true, transactionId: "123" }`.

---

### 5. Decorator Pattern (Structural)
- **Vấn đề:** Muốn bổ sung tính năng Caching hay Auth Guard xung quanh một hàm có sẵn mà không được sửa code gốc của hàm đó.
- **Giải pháp:** Bọc hàm gốc bên trong một Class/Function Decorator (Chính là cơ chế `@UseGuards()`, `@Get()` của NestJS).

---

## 🚀 3. LỜI KHUYÊN HỌC ANKI DECK 01 HÔM NAY:
1. Master trọn vẹn **6 Pattern Tier 1** và **5 Pattern Tier 2**.
2. **Nguyên tắc "Code Replacement":** Khi lật thẻ Anki, luôn tự hỏi: *"Pattern này sinh ra để thay thế đoạn code xấu nào trong NestJS/TS?"*
3. Đối với các Pattern Tier 4 (*Visitor, Interpreter, Flyweight, Memento, Bridge, Prototype*), lướt qua 2 giây để biết khái niệm, không tốn thời gian học thuộc!
