# 🏆 GOF & ARCHITECTURAL DESIGN PATTERNS: HIGH-ROI STUDY GUIDE

> **Author:** Duong Phuc Khanh (Senior Fullstack & System Architect)  
> **Purpose:** Xếp hạng 23 GoF Design Patterns theo tỷ lệ ROI (High Return on Investment) — Ưu tiên học các Pattern dùng nhiều nhất trong Backend/NestJS hàng ngày, loại bỏ việc nhồi nhét học thuộc lòng không thực tế.

---

## 📊 1. BẢNG XẾP HẠNG HIGH-ROI DESIGN PATTERNS MATRIX

| Tier / Mức ưu tiên | Pattern Name | Nhóm GoF | Tần suất dùng trong BE | Độ khó học | Tác dụng giải quyết vấn đề (Use Case chính) |
|---|---|---|---|---|---|
| **Tier 1 (MUST-KNOW)** | **Strategy** | Behavioral | 🔥 Rất cao (Hàng ngày) | 🟢 Dễ | Xóa sạch if-else / switch-case chật chội. Thay đổi thuật toán linh hoạt (Payment, Pricing). |
| **Tier 1 (MUST-KNOW)** | **Factory Method** | Creational | 🔥 Rất cao (Hàng ngày) | 🟢 Dễ | Tạo Instance đối tượng động dựa vào tham số (Payment Gateway, Noti Provider). |
| **Tier 1 (MUST-KNOW)** | **Observer / Pub-Sub** | Behavioral | 🔥 Rất cao (Hàng ngày) | 🟢 Dễ | Phát Event bất đồng bộ (UserRegistered -> Gửi Email, Tạo Ví, Index Search). |
| **Tier 1 (MUST-KNOW)** | **Singleton** | Creational | 🔥 Rất cao (Hàng ngày) | 🟢 Dễ | Đảm bảo đúng 1 Instance duy nhất (DB Connection Pool, Redis Client, NestJS Service). |
| **Tier 1 (MUST-KNOW)** | **Decorator** | Structural | 🔥 Rất cao (Hàng ngày) | 🟡 Vừa | Bọc thêm tính năng (NestJS @UseGuards(), Cache Wrapper bọc quanh DB Repository). |
| **Tier 1 (MUST-KNOW)** | **Adapter** | Structural | 🔥 Rất cao (Hàng ngày) | 🟢 Dễ | Chuẩn hóa API bên thứ ba (VNPay/Stripe payload) về DTO nội bộ của hệ thống. |
| **Tier 2 (HIGH-VALUE)** | **Chain of Responsibility**| Behavioral | 🟡 Cao (Thường xuyên) | 🟢 Dễ | Xây dựng Middleware Pipeline (Auth -> Role Check -> Rate Limit -> Handler). |
| **Tier 2 (HIGH-VALUE)** | **State** | Behavioral | 🟡 Cao (Thường xuyên) | 🟡 Vừa | Quản lý State Machine đơn hàng (CREATED -> PAID -> SHIPPED -> CANCELLED). |
| **Tier 2 (HIGH-VALUE)** | **Builder** | Creational | 🟡 Cao (Thường xuyên) | 🟢 Dễ | Dựng các Query SQL phức tạp (Knex/Prisma query builder) hoặc Test Data Fixtures. |
| **Tier 2 (HIGH-VALUE)** | **Repository & UoW** | Architecture | 🟡 Cao (Thường xuyên) | 🟡 Vừa | Cách ly ORM/DB khỏi Business Logic + Quản lý DB Transaction nguyên tử. |
| **Tier 2 (HIGH-VALUE)** | **Proxy** | Structural | 🟡 Cao (Thường xuyên) | 🟡 Vừa | Kiểm soát truy cập (Security Proxy, Lazy Loading heavy objects, Reverse Proxy Nginx). |
| **Tier 3 (NICHE/RARE)** | **Command** | Behavioral | 🔵 Trung bình | 🟡 Vừa | Undo/Redo, Queueing CLI Tasks. |
| **Tier 3 (NICHE/RARE)** | **Template Method** | Behavioral | 🔵 Trung bình | 🟢 Dễ | Khung thuật toán cố định ở Abstract Class cho class con override. |
| **Tier 3 (NICHE/RARE)** | **Facade** | Structural | 🔵 Trung bình | 🟢 Dễ | Gom nhiều subsystem phức tạp đằng sau 1 API đơn giản. |
| **Tier 4 (LOW-ROI)** | *Flyweight, Memento, Visitor, Interpreter, Bridge, Prototype* | Các nhóm | ⚪ Rất thấp (Hiếm gặp) | 🔴 Khó | Thường nằm sâu bên trong Framework Core / Compiler Engine. Không cần ưu tiên học thuộc. |

---

## 🎯 2. CHI TIẾT CÁC PATTERN TIER 1 (CẦN NẮM NẰM LÒNG VÀO ANKI)

### 1. Strategy Pattern (Behavioral)
- **Vấn đề:** Có 10 phương thức thanh toán (VNPAY, MOMO, PAYPAL, STRIPE...). Nếu dùng if-else thì file code dài 1,000 dòng, mỗi lần thêm cổng mới phải sửa file cũ (Vi phạm nguyên lý SOLID - Open/Closed Principle).
- **Giải pháp:** Định nghĩa 1 Interface PaymentStrategy với hàm pay(amount). Mỗi cổng thanh toán là 1 class triển khai interface đó.
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
- **Vấn đề:** Client không cần biết chi tiết khởi tạo một class phức tạp như nào, chỉ cần truyền vào tham số type ('EMAIL', 'SMS', 'PUSH').
- **Giải pháp:** Tạo class Factory chứa hàm createNotification(type) trả về đúng Provider tương ứng.

---

### 3. Observer / Pub-Sub Pattern (Behavioral)
- **Vấn đề:** Khi hành động UserRegistered xảy ra, ta muốn gửi Email chào mừng, tạo Wallet 0đ, và đẩy data sang Analytics mà không làm nghẽn hàm đăng ký.
- **Giải pháp:** Publisher phát sự kiện UserRegisteredEvent. Các Observer (EmailSubscriber, WalletSubscriber) đăng ký lắng nghe và tự động chạy độc lập bất đồng bộ.

---

### 4. Adapter Pattern (Structural)
- **Vấn đề:** Cổng thanh toán VNPay trả về { vnp_ResponseCode: "00", vnp_TxnRef: "123" }, trong khi Stripe trả về { status: "succeeded", id: "ch_123" }.
- **Giải pháp:** Dùng Adapter chuyển đổi cả 2 định dạng khác nhau này về đúng 1 DTO chuẩn nội bộ: { success: true, transactionId: "123" }.

---

### 5. Decorator Pattern (Structural)
- **Vấn đề:** Muốn bổ sung tính năng Caching hay Auth Guard xung quanh một hàm có sẵn mà không được sửa code gốc của hàm đó.
- **Giải pháp:** Bọc hàm gốc bên trong một Class/Function Decorator (Chính là cơ chế @UseGuards(), @Get() của NestJS).

---

## 🚀 3. LỜI KHUYÊN HỌC ANKI DECK 01 HÔM NAY:
1. Tập trung **master 6 Pattern Tier 1** và **5 Pattern Tier 2**.
2. Khi lật thẻ Anki, luôn tự hỏi: *"Pattern này dùng để thay thế cho cái gì trong code NestJS/TypeScript?"* (ví dụ: Strategy thay thế cho if-else / switch-case).
3. Đối với các Pattern Tier 4 (*Visitor, Interpreter, Flyweight*), lướt nhanh để biết khái niệm, không tốn thời gian học thuộc!
