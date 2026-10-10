"""Interfrange des fentes d'Young : i = lambda * D / a (notes/fentes-young.md)."""


def interfrange(longueur_onde, distance_ecran, ecart_fentes):
    """Toutes les longueurs en mètres ; renvoie l'interfrange en mètres."""
    return longueur_onde * distance_ecran / ecart_fentes


if __name__ == "__main__":
    lam, a, d = 650e-9, 0.2e-3, 2.0
    print(f"lambda = {lam * 1e9:.0f} nm, a = {a * 1e3:.1f} mm, D = {d:.1f} m -> interfrange i = {interfrange(lam, d, a) * 1e3:.2f} mm")
