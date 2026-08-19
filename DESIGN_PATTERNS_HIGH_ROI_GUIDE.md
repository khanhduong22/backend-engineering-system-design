# 🏆 GOF & ARCHITECTURAL DESIGN PATTERNS: HIGH-ROI STUDY GUIDE

> **Author:** Duong Phuc Khanh (Senior Fullstack & System Architect)  
> **Purpose:** Xếp hạng trọn bộ 23 GoF Design Patterns theo TIERS (High Return on Investment) — Ưu tiên học các Pattern dùng nhiều nhất trong Backend/NestJS hàng ngày, loại bỏ việc nhồi nhét học thuộc lòng không thực tế.

---

## 📊 1. DANH SÁCH TRỌN BỘ 23 GOF DESIGN PATTERNS (XẾP THEO TIER KHUYÊN DÙNG)

### 🔥 TIER 1: MUST-KNOW (6 Patterns - Dùng hàng ngày trong Backend / NestJS)
| STT | Pattern Name | Nhóm GoF | Tần suất trong BE | Tác dụng & Use Case chính |
|---|---|---|---|---|
| 1 | **Strategy** | Behavioral | 🔥 Rất cao | Thay thế `if-else` / `switch-case` chật chội. Đổi thuật toán linh hoạt (Payment, Pricing). |
| 2 | **Factory Method** | Creational | 🔥 Rất cao | Tạo đối tượng động dựa vào tham số đầu vào (`type: 'EMAIL' | 'SMS'`). |
| 3 | **Observer / Pub-Sub** | Behavioral | 🔥 Rất cao | Phát Event bất đồng bộ (`UserRegistered` -> Gửi Noti, Tạo Ví, Index Search). |
| 4 | **Singleton** | Creational | 🔥 Rất cao | Đảm bảo 1 Instance duy nhất (DB Pool, Redis Client, NestJS `@Injectable()`). |
| 5 | **Decorator** | Structural | 🔥 Rất cao | Bọc thêm tính năng (NestJS `@UseGuards()`, Caching Wrapper bọc Repository). |
| 6 | **Adapter** | Structural | 🔥 Rất cao | Chuẩn hóa API 3rd-party (VNPay/Stripe payload) về DTO nội bộ của hệ thống. |

---

### 🟡 TIER 2: HIGH-VALUE (5 Patterns - Dùng thường xuyên trong Kiến trúc Phân tán / Clean Architecture)
| STT | Pattern Name | Nhóm GoF | Tần suất trong BE | Tác dụng & Use Case chính |
|---|---|---|---|---|
| 7 | **Chain of Responsibility**| Behavioral | 🟡 Cao | Xây dựng Middleware Pipeline (Auth -> Role Check -> Rate Limit -> Handler). |
| 8 | **State** | Behavioral | 🟡 Cao | Quản lý State Machine đơn hàng (`CREATED` -> `PAID` -> `SHIPPED` -> `CANCELLED`). |
| 9 | **Builder** | Creational | 🟡 Cao | Dựng đối tượng phức tạp nhiều bước (SQL Query Builder, Test Data Fixtures). |
| 10 | **Proxy** | Structural | 🟡 Cao | Control truy cập (Security Proxy, Lazy Loading, Nginx Reverse Proxy). |
| 11 | **Iterator** | Behavioral | 🟡 Cao | Duyệt qua tập hợp dữ liệu (`for...of`, Async Generator functions). |

---

### 🔵 TIER 3: NICHE / RARE (5 Patterns - Dùng cho các bài toán đặc thù)
| STT | Pattern Name | Nhóm GoF | Tần suất trong BE | Tác dụng & Use Case chính |
|---|---|---|---|---|
| 12 | **Abstract Factory** | Creational | 🔵 Trung bình | Tạo họ các đối tượng liên quan (VD: Cross-platform DB Client Factory). |
| 13 | **Command** | Behavioral | 🔵 Trung bình | Đóng gói Request thành Object (Undo/Redo, Queueing CLI commands). |
| 14 | **Template Method** | Behavioral | 🔵 Trung bình | Định nghĩa khung thuật toán cố định ở Abstract Class cho class con override. |
| 15 | **Facade** | Structural | 🔵 Trung bình | Gom nhiều subsystem phức tạp đằng sau 1 API interface đơn giản. |
| 16 | **Composite** | Structural | 🔵 Trung bình | Quản lý cấu trúc cây đệ quy (File/Folder tree, Nested Menu multi-level). |

---

### ⚪ TIER 4: LOW-ROI (7 Patterns - Rất hiếm gặp / Chủ yếu nằm trong Framework Core)
| STT | Pattern Name | Nhóm GoF | Tần suất trong BE | Tác dụng & Use Case chính |
|---|---|---|---|---|
| 17 | **Prototype** | Creational | ⚪ Hiếm gặp | Clone đối tượng có sẵn (dùng `clone()` deep copy). |
| 18 | **Bridge** | Structural | ⚪ Hiếm gặp | Tách Abstraction khỏi Implementation (ít dùng trong BE hiện đại). |
| 19 | **Flyweight** | Structural | ⚪ Hiếm gặp | Chia sẻ bộ nhớ cho hàng ngàn đối tượng giống nhau (Game Engine). |
| 20 | **Mediator** | Behavioral | ⚪ Hiếm gặp | Trung gian giao tiếp giảm phụ thuộc chéo (Chat room server, Event Bus). |
| 21 | **Memento** | Behavioral | ⚪ Hiếm gặp | Lưu và khôi phục Snapshot trạng thái cũ của Object (Undo state). |
| 22 | **Visitor** | Behavioral | ⚪ Hiếm gặp | Thêm thuật toán mới vào class mà không sửa class đó (Compiler AST). |
| 23 | **Interpreter** | Behavioral | ⚪ Hiếm gặp | Xây dựng bộ đọc/dịch ngôn ngữ/cú pháp riêng (Regex, SQL Parser). |

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
