class PaymentMethod:
    """Base class for payment types."""
    
    def __init__(self, method_name: str):
        self.method_name = method_name

    def process_payment(self, amount: float) -> bool:
        """Abstract method to process payments."""
        raise NotImplementedError


class CreditCard(PaymentMethod):
    """Implements credit card payment."""
    
    def __init__(self, card_number: str, holder_name: str):
        super().__init__("Credit Card")
        self.__card_number = card_number #now Private CE
        self.__holder_name = holder_name #now Private CE

    def process_payment(self, amount: float) -> bool:
        """Process a credit card payment."""
        print(f"Charging ${amount:.2f} to card {self.card_number[-4:]}...")
        return True


class PayPal(PaymentMethod):
    """Implements PayPal payment."""
    
    def __init__(self, email: str):
        super().__init__("PayPal")
        self._email = email #Protected CE

    def process_payment(self, amount: float) -> bool:
        """Process a PayPal payment."""
        print(f"Processing PayPal payment of ${amount:.2f} from {self._email}...")
        return True


class Klarna(PaymentMethod):
    """Implements Klarna payment (Buy Now, Pay Later)."""

    def __init__(self, account_id: str, installments: int = 4):
        super().__init__("Klarna")
        self._account_id = account_id      # protected (less sensitive)
        self._installments = installments  # protected

    @property
    def account_id(self):
        return self._account_id

    @property
    def installments(self):
        return self._installments

    def process_payment(self, amount: float) -> bool:
        """Process a Klarna payment in installments."""
        installment_amount = amount / self._installments
        print(
            f"Processing Klarna payment of ${amount:.2f} "
            f"as {self._installments} installments of ${installment_amount:.2f} "
            f"for account {self._account_id}..."
        )
        return True
