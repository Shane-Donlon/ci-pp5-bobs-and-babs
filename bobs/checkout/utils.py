import stripe


def create_stripe_customer(full_name, email, stripe_token, transaction_id):
    return stripe.Customer.create(
        name=full_name,
        email=email,
        source=stripe_token,
        description=transaction_id
    )


def create_stripe_charge(customer, total, transaction_id):
    return stripe.Charge.create(
        amount=total,
        currency="eur",
        description=f"Payment for order{transaction_id}",
        customer=customer,
    )


def create_stripe_invoice(customer, total, transaction_id):
    invoice_item = stripe.InvoiceItem.create(
        customer=customer.id,
        amount=total,
        currency="eur",
        description=f"Payment for order{transaction_id}",
    )

    invoice = stripe.Invoice.create(
        customer=customer.id,
        auto_advance=True  # Auto-finalize this draft after ~1 hour
    )
    invoice.finalize_invoice()

    return invoice
