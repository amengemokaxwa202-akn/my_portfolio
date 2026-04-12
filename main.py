import flet as ft

def main(page: ft.Page):
    # ===== PAGE SETUP =====
    page.title = "Civil Engineering Portfolio"
    page.theme_mode = "light"
    page.padding = 20
    page.scroll = "adaptive"
    page.bgcolor = "#F5F7FA"
    
    # ===== COLOR THEME =====
    PRIMARY_COLOR = "#1E3A5F"
    SECONDARY_COLOR = "#4A90E2"
    ACCENT_COLOR = "#FF6B35"
    CARD_BG = "#FFFFFF"
    TEXT_DARK = "#2C3E50"
    TEXT_LIGHT = "#7F8C8D"
    
    # ===== CONTENT AREA =====
    content_area = ft.Column(spacing=20)
    
    # ===== NAVIGATION FUNCTION =====
    def navigate_to(section):
        if section == "home":
            show_home()
        elif section == "timeline":
            show_timeline()
        elif section == "matlab":
            show_matlab()
        elif section == "blog":
            show_blog()
        elif section == "github":
            show_github()
        page.update()
    
    # ===== HOME PAGE =====
    def show_home():
        content_area.controls = [
        # Hero Section with Picture
        ft.Container(
            content=ft.Row([
                # Left side - Text
                ft.Column([
                    ft.Text("👋 Hello, I'm", size=18, color=TEXT_LIGHT),
                    ft.Text("Amenge KN Mokaxwa", size=45, weight="bold", color=PRIMARY_COLOR),
                    ft.Text("3rd Year EXT Civil Engineering Student", size=20, color=SECONDARY_COLOR),
                    ft.Text("JEDS UNAM", size=16, color=TEXT_LIGHT, italic=True),
                    ft.Divider(height=2, color=ACCENT_COLOR),
                    ft.Container(height=10),
                    ft.Text("Welcome to my portfolio website!", size=16, color=TEXT_DARK),
                    ft.Text("This site showcases my work in the Computing Programming module.", size=14, color=TEXT_LIGHT),
                ], expand=True, spacing=10),
                
                # Right side - Profile Picture
                ft.Container(
                    content=ft.CircleAvatar(
                        content=ft.Text("👩‍💻", size=40),
                        color=ft.Colors.WHITE,
                        bgcolor=SECONDARY_COLOR,
                        radius=70,
                    ),
                ),
            ], alignment="center"),
            padding=40,
            bgcolor=CARD_BG,
            border_radius=20,
        ),
        
        # Clickable Stats Cards (FIXED)
        ft.Row([
            ft.GestureDetector(
                content=ft.Card(
                    content=ft.Container(
                        content=ft.Column([
                            ft.Text("📚", size=30),
                            ft.Text("8 MATLAB Courses", size=16, weight="bold"),
                            ft.Text("Click to view →", size=10, color=SECONDARY_COLOR),
                        ], horizontal_alignment="center", spacing=5),
                        padding=20,
                        width=200,
                    ),
                ),
                on_tap=lambda e: navigate_to("matlab"),
            ),
            ft.GestureDetector(
                content=ft.Card(
                    content=ft.Container(
                        content=ft.Column([
                            ft.Text("💻", size=30),
                            ft.Text("4 Projects", size=16, weight="bold"),
                            ft.Text("Click to view →", size=10, color=SECONDARY_COLOR),
                        ], horizontal_alignment="center", spacing=5),
                        padding=20,
                        width=200,
                    ),
                ),
                on_tap=lambda e: navigate_to("timeline"),
            ),
            ft.GestureDetector(
                content=ft.Card(
                    content=ft.Container(
                        content=ft.Column([
                            ft.Text("🐙", size=30),
                            ft.Text("15+ Commits", size=16, weight="bold"),
                            ft.Text("Click to view →", size=10, color=SECONDARY_COLOR),
                        ], horizontal_alignment="center", spacing=5),
                        padding=20,
                        width=200,
                    ),
                ),
                on_tap=lambda e: navigate_to("github"),
            ),
        ], alignment="center", spacing=20, wrap=True),
        
        # About Section
        ft.Container(
            content=ft.Column([
                ft.Text("About This Portfolio", size=24, weight="bold", color=PRIMARY_COLOR),
                ft.Text("This website serves as my individual portfolio for the Computing Programming module. It documents my journey through MATLAB certification, technical writing, and GitHub collaboration.", size=14),
                ft.Container(height=10),
                ft.Text("📌 Key Sections:", weight="bold", size=16),
                ft.Text("• Project Timeline - Weekly logs of my contributions", size=14),
                ft.Text("• MATLAB Hub - Proof of 8 completed courses", size=14),
                ft.Text("• Technical Blog - Engineering concepts with formulas", size=14),
                ft.Text("• GitHub Evidence - Verifiable commit history", size=14),
            ], spacing=15),
            padding=30,
            bgcolor=CARD_BG,
            border_radius=20,
        ),
    ]
    page.update()
    
    # ===== TIMELINE PAGE =====
    def show_timeline():
        content_area.controls = [
            ft.Text("📅 Project Timeline", size=30, weight="bold", color=PRIMARY_COLOR),
            ft.Text("My individual contributions to the group project", size=14, color=TEXT_LIGHT),
            ft.Divider(),
            ft.Container(
                content=ft.Column([
                    ft.Text("Week 1-2: Project Setup", size=18, weight="bold", color=SECONDARY_COLOR),
                    ft.Text("✓ Created GitHub repository", size=13),
                    ft.Text("✓ Installed Flet framework", size=13),
                    ft.Text("✓ Designed portfolio structure", size=13),
                ]),
                padding=15,
                bgcolor=CARD_BG,
                border_radius=10,
            ),
            ft.Container(
                content=ft.Column([
                    ft.Text("Week 3-4: Core Development", size=18, weight="bold", color=SECONDARY_COLOR),
                    ft.Text("✓ Built navigation system", size=13),
                    ft.Text("✓ Implemented all 5 pages", size=13),
                    ft.Text("✓ Added responsive layout", size=13),
                ]),
                padding=15,
                bgcolor=CARD_BG,
                border_radius=10,
            ),
            ft.Container(
                content=ft.Column([
                    ft.Text("Week 5-6: Content Creation", size=18, weight="bold", color=SECONDARY_COLOR),
                    ft.Text("✓ Wrote technical blog posts", size=13),
                    ft.Text("✓ Added mathematical formulas", size=13),
                    ft.Text("✓ Uploaded MATLAB certificates", size=13),
                ]),
                padding=15,
                bgcolor=CARD_BG,
                border_radius=10,
            ),
            ft.Container(
                content=ft.Column([
                    ft.Text("Week 7-8: GitHub & Deployment", size=18, weight="bold", color=SECONDARY_COLOR),
                    ft.Text("✓ Documented commit history", size=13),
                    ft.Text("✓ Created pull requests", size=13),
                    ft.Text("✓ Deployed to GitHub Pages", size=13),
                ]),
                padding=15,
                bgcolor=CARD_BG,
                border_radius=10,
            ),
        ]
        page.update()
    
    # ===== MATLAB PAGE =====
    def show_matlab():
        courses = ["MATLAB Onramp", "Simulink Onramp", "Machine Learning Onramp", "Deep Learning Onramp", "Image Processing Onramp", "Signal Processing Onramp", "Control Design Onramp", "Stateflow Onramp"]
        
        course_list = ft.Column(spacing=10)
        for course in courses:
            course_list.controls.append(
                ft.Container(
                    content=ft.Row([
                        ft.Text("✅", size=20),
                        ft.Text(course, size=14, expand=True),
                        ft.Text("Completed", size=12, color="green"),
                    ]),
                    padding=10,
                    bgcolor=CARD_BG,
                    border_radius=8,
                )
            )
        
        content_area.controls = [
            ft.Text("🏆 MATLAB Achievement Hub", size=30, weight="bold", color=PRIMARY_COLOR),
            ft.Text("8 Self-Paced Courses from MathWorks Learning Center", size=14, color=TEXT_LIGHT),
            ft.Divider(),
            ft.ProgressBar(value=1.0, width=400, color="green"),
            ft.Text("100% Complete - All 8 Courses Finished!", size=14, color="green", weight="bold"),
            ft.Container(height=20),
            ft.Text("📚 Completed Courses:", size=20, weight="bold", color=PRIMARY_COLOR),
            course_list,
            ft.Container(
                content=ft.Column([
                    ft.Text("📸 Certificate Screenshots", size=16, weight="bold"),
                    ft.Text("[Place your MATLAB certificate screenshots here]", size=12, italic=True),
                ], horizontal_alignment="center"),
                padding=20,
                bgcolor="#FFF3E0",
                border_radius=10,
            ),
        ]
        page.update()
    
    # ===== BLOG PAGE =====
    def show_blog():
        content_area.controls = [
            ft.Text("✍️ Technical Blog", size=30, weight="bold", color=PRIMARY_COLOR),
            ft.Text("Confidence in Concepts - Engineering Explained", size=14, color=TEXT_LIGHT),
            ft.Divider(),
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text("📐 Beam Deflection in Structural Engineering", size=18, weight="bold"),
                        ft.Text("Posted: March 2025", size=11, color=TEXT_LIGHT),
                        ft.Divider(),
                        ft.Text("The maximum deflection of a simply supported beam under uniform load:", size=13),
                        ft.Container(
                            content=ft.Text("δ_max = (5wL⁴) / (384EI)", size=18, weight="bold", italic=True),
                            padding=15,
                            bgcolor="#FFF3E0",
                            border_radius=8,
                        ),
                        ft.Text("Where:", size=13, weight="bold"),
                        ft.Text("• w = uniform load per unit length", size=12),
                        ft.Text("• L = beam length", size=12),
                        ft.Text("• E = modulus of elasticity", size=12),
                        ft.Text("• I = moment of inertia", size=12),
                    ], spacing=10),
                    padding=20,
                ),
            ),
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text("💰 Material Cost Optimization", size=18, weight="bold"),
                        ft.Text("Posted: March 2025", size=11, color=TEXT_LIGHT),
                        ft.Divider(),
                        ft.Text("Total material cost including overheads:", size=13),
                        ft.Container(
                            content=ft.Text("Total Cost = Σ(Qᵢ × Pᵢ) + Overheads", size=18, weight="bold", italic=True),
                            padding=15,
                            bgcolor="#E8F5E9",
                            border_radius=8,
                        ),
                        ft.Text("Where:", size=13, weight="bold"),
                        ft.Text("• Qᵢ = Quantity of material i", size=12),
                        ft.Text("• Pᵢ = Price per unit of material i", size=12),
                        ft.Text("• n = Number of different materials", size=12),
                    ], spacing=10),
                    padding=20,
                ),
            ),
        ]
        page.update()
    
    # ===== GITHUB PAGE =====
    def show_github():
        content_area.controls = [
            ft.Text("🐙 GitHub Evidence", size=30, weight="bold", color=PRIMARY_COLOR),
            ft.Text("Verifiable individual contributions", size=14, color=TEXT_LIGHT),
            ft.Divider(),
            ft.Row([
                ft.Card(content=ft.Container(content=ft.Column([ft.Text("📊", size=30), ft.Text("15", size=28, weight="bold"), ft.Text("Commits", size=12)], horizontal_alignment="center"), padding=20, width=150)),
                ft.Card(content=ft.Container(content=ft.Column([ft.Text("🔄", size=30), ft.Text("3", size=28, weight="bold"), ft.Text("Pull Requests", size=12)], horizontal_alignment="center"), padding=20, width=150)),
                ft.Card(content=ft.Container(content=ft.Column([ft.Text("👥", size=30), ft.Text("5", size=28, weight="bold"), ft.Text("Code Reviews", size=12)], horizontal_alignment="center"), padding=20, width=150)),
            ], alignment="center", spacing=20, wrap=True),
            ft.Container(
                content=ft.Column([
                    ft.Text("💡 Impact Summary", size=20, weight="bold", color=PRIMARY_COLOR),
                    ft.Text("✅ Implemented material cost calculator using Σ formula", size=13),
                    ft.Text("✅ Fixed unit conversion bug affecting beam deflection", size=13),
                    ft.Text("✅ Added validation for structural load inputs", size=13),
                    ft.Text("✅ Documented civil engineering modules for team", size=13),
                ], spacing=10),
                padding=20,
                bgcolor=CARD_BG,
                border_radius=10,
            ),
            ft.Container(
                content=ft.Column([
                    ft.Text("📸 GitHub Screenshots", size=16, weight="bold"),
                    ft.Text("[Insert commit history screenshot here]", size=12, italic=True),
                    ft.Text("[Insert pull request logs screenshot here]", size=12, italic=True),
                ], horizontal_alignment="center", spacing=10),
                padding=20,
                bgcolor="#F0F0F0",
                border_radius=10,
            ),
            ft.Text("⚠️ Replace placeholder screenshots with actual GitHub screenshots", size=11, color="red", italic=True),
        ]
        page.update()
    
    # ===== NAVIGATION BAR =====
    navbar = ft.Container(
        content=ft.Row([
            ft.Text("🚀 My Portfolio", size=22, weight="bold", color=PRIMARY_COLOR),
            ft.Row([
                ft.TextButton("Home", on_click=lambda e: navigate_to("home")),
                ft.TextButton("Timeline", on_click=lambda e: navigate_to("timeline")),
                ft.TextButton("MATLAB", on_click=lambda e: navigate_to("matlab")),
                ft.TextButton("Blog", on_click=lambda e: navigate_to("blog")),
                ft.TextButton("GitHub", on_click=lambda e: navigate_to("github")),
            ], spacing=20),
        ], alignment="spaceBetween"),
        padding=15,
        bgcolor=CARD_BG,
    )
    
    # ===== ADD EVERYTHING TO PAGE =====
    page.add(navbar)
    page.add(content_area)
    
    # Start with home page
    show_home()

# Run the app
ft.app(target=main)