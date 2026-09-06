import type { Metadata } from "next"
import { Inter } from "next/font/google"
import "./globals.css"

const inter = Inter({ subsets: ["latin"] })

export const metadata: Metadata = {
  title: "Educ.Infos224 - L'actualité de l'éducation en Guinée",
  description: "Educ Infos 224 est une plateforme d'information spécialisée dans l'actualité de l'éducation en Guinée. Nous informons, expliquons et valorisons les réformes, les innovations et les initiatives qui contribuent à bâtir un système éducatif plus performant.",
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="fr">
      <body className={inter.className}>{children}</body>
    </html>
  )
}
