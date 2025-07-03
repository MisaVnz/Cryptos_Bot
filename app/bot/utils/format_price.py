"""Función para formatear el precio de una criptomoneda."""

def format_price(price, symbol):
    return f"💰 {symbol}: ${price:,.2f}" if price else "❌ Error al obtener precio"