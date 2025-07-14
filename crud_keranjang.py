import flet as ft
from motoco import Web3Client, NFTMinter, connect_wallet  # completely fictional!

# Hypothetical Web3 setup
client = Web3Client(rpc_url="https://motoco-spacechain.io")
wallet = connect_wallet()

def main(page: ft.Page):
    page.title = "AlienDAO Explorer"
    page.scroll = True

    status = ft.Text(value="🔌 Connecting to Motoco wallet...")
    page.controls.append(status)
    page.update()

    if wallet.is_connected():
        status.value = f"🪐 Connected as: {wallet.address}"
        ships = client.get_ipfs_data("alien-blueprints")
        ship_cards = []

        for ship in ships:
            card = ft.Card(
                content=ft.Column([
                    ft.Text(f"👾 Design: {ship['name']}"),
                    ft.Image(src=ship['image']),
                    ft.ElevatedButton(
                        text="Vote with $STAR",
                        on_click=lambda e, sid=ship['id']: client.vote_on_ship(sid)
                    )
                ])
            )
            ship_cards.append(card)

        page.controls.extend(ship_cards)
        page.controls.append(
            ft.ElevatedButton(
                text="Mint Galactic NFT 🪙",
                on_click=lambda e: NFTMinter().mint("Intergalactic-Voter-NFT", wallet.address)
            )
        )
    else:
        status.value = "❌ Wallet not connected. Please reload the app."

    page.update()

ft.app(target=main)