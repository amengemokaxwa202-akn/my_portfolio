import logging  
import flet as ft
import os

def main(page: ft.Page):
    # ===== PAGE SETUP =====
    page.title = "Amenge Mokaxwa | Civil Engineering & Metallurgy Portfolio"
    page.theme_mode = "light"
    page.padding = 30
    page.scroll = "adaptive"
    page.bgcolor = "#F8FAFC"  
    
    # ===== COLOR THEME =====
    PRIMARY_COLOR = "#0F172A"    
    SECONDARY_COLOR = "#2563EB"  
    CARD_BG = "#FFFFFF"
    TEXT_DARK = "#1E293B"
    TEXT_LIGHT = "#64748B"
    BORDER_COLOR = "#E2E8F0"
    
    # ===== NAVIGATION BAR (Persistent) =====
    navbar = ft.Container(
        content=ft.Row([
            ft.Text("TECHNICAL PORTFOLIO", size=16, weight="bold", color=PRIMARY_COLOR),
            ft.Row([
                ft.TextButton("Home", on_click=lambda e: navigate_to("home")),
                ft.TextButton("Timeline", on_click=lambda e: navigate_to("timeline")),
                ft.TextButton("MATLAB", on_click=lambda e: navigate_to("matlab")),
                ft.TextButton("Blog", on_click=lambda e: navigate_to("blog")),
                ft.TextButton("GitHub Audit", on_click=lambda e: navigate_to("github")),
            ], spacing=10),
        ], alignment="spaceBetween"),
        padding=ft.Padding.only(bottom=15),
        border=ft.Border.only(bottom=ft.BorderSide(1, BORDER_COLOR))
    )
    
    # ===== NAVIGATION ROUTER =====
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
    
    # ===== 1. HOME VIEW =====
    def show_home():
        page.controls = [
            navbar,
            ft.Container(
                content=ft.Row([
                    ft.Column([
                        ft.Text("TECHNICAL PORTFOLIO", size=12, weight="bold", color=SECONDARY_COLOR),
                        ft.Text("Amenge KN Mokaxwa", size=40, weight="bold", color=PRIMARY_COLOR),
                        ft.Text("3rd Year Civil Engineering Student (EXT)", size=18, weight="w500", color=TEXT_LIGHT),
                        ft.Text("JEDS | University of Namibia", size=14, color=TEXT_LIGHT, italic=True),
                        ft.Container(height=5),
                        ft.Text(
                            "Welcome to my technical portfolio. This platform showcases individual contributions, "
                            "applied computing proficiencies, and foundational engineering documentation.", 
                            size=15, color=TEXT_DARK, max_lines=3
                        ),
                    ], expand=True, spacing=8),
                    
                    ft.Container(
                        content=ft.Image(
                            src="images/profile.jpeg",  
                            width=120,
                            height=120,
                            fit="cover",
                            border_radius=60,
                        ),
                        padding=10,
                    ),
                ], alignment="spaceBetween", vertical_alignment="center"),
                padding=40,
                bgcolor=CARD_BG,
                border=ft.Border.all(1, BORDER_COLOR),
                border_radius=12,
            ),
            
            ft.Row([
                ft.GestureDetector(
                    content=ft.Container(
                        content=ft.Column([
                            ft.Text("MATLAB CORE", size=11, weight="bold", color=TEXT_LIGHT),
                            ft.Text("8 Courses", size=22, weight="bold", color=PRIMARY_COLOR),
                            ft.Text("View Certificates →", size=11, color=SECONDARY_COLOR, weight="w500"),
                        ], spacing=4),
                        padding=20,
                        bgcolor=CARD_BG,
                        border=ft.Border.all(1, BORDER_COLOR),
                        border_radius=8,
                        width=220,
                    ),
                    on_tap=lambda e: navigate_to("matlab"),
                ),
                ft.GestureDetector(
                    content=ft.Container(
                        content=ft.Column([
                            ft.Text("PROJECT LOGS", size=11, weight="bold", color=TEXT_LIGHT),
                            ft.Text("4 Milestones", size=22, weight="bold", color=PRIMARY_COLOR),
                            ft.Text("View Timeline →", size=11, color=SECONDARY_COLOR, weight="w500"),
                        ], spacing=4),
                        padding=20,
                        bgcolor=CARD_BG,
                        border=ft.Border.all(1, BORDER_COLOR),
                        border_radius=8,
                        width=220,
                    ),
                    on_tap=lambda e: navigate_to("timeline"),
                ),
                ft.GestureDetector(
                    content=ft.Container(
                        content=ft.Column([
                            ft.Text("VERSION CONTROL", size=11, weight="bold", color=TEXT_LIGHT),
                            ft.Text("15+ Commits", size=22, weight="bold", color=PRIMARY_COLOR),
                            ft.Text("View Evidence →", size=11, color=SECONDARY_COLOR, weight="w500"),
                        ], spacing=4),
                        padding=20,
                        bgcolor=CARD_BG,
                        border=ft.Border.all(1, BORDER_COLOR),
                        border_radius=8,
                        width=220,
                    ),
                    on_tap=lambda e: navigate_to("github"),
                ),
            ], alignment="center", spacing=20, wrap=True),
        ]
        page.update()
    
    # ===== 2. TIMELINE VIEW =====
    def show_timeline():
        timeline_data = [
            ("Weeks 1 - 2", "Environment Initialization & Architecture Setup", ["Set up local Flet/Python directory structure and base framework.", "Designed dynamic navigation logic for sub-view swapping across sections."]),
            ("Weeks 3 - 4", "Metallurgical Data Modeling & UI Layout", ["Built Firestore collection schema mappings for mineral sample classification.", "Programmed state logic for input validation within core technician views."]),
            ("Weeks 5 - 6", "Technical Writing & Mathematical Model Translation", ["Drafted structural performance modules for documentation.", "Embedded analytical formulas for max deflection calculations to match guidelines."]),
            ("Weeks 7 - 8", "Version Deployment & Peer Reviews", ["Audited open branch code assets and finalized git pull integration tracking.", "Conducted manual security exception handling tests on administrative view bounds."])
        ]
        
        timeline_cards = []
        for period, title, tasks in timeline_data:
            task_lines = ft.Column([ft.Text(f"  • {task}", size=13, color=TEXT_DARK) for task in tasks], spacing=4)
            timeline_cards.append(
                ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Text(period, size=12, weight="bold", color=SECONDARY_COLOR),
                            ft.Text(f"|  {title}", size=15, weight="bold", color=PRIMARY_COLOR),
                        ]),
                        ft.Container(height=2),
                        task_lines
                    ], spacing=5),
                    padding=20,
                    bgcolor=CARD_BG,
                    border=ft.Border.all(1, BORDER_COLOR),
                    border_radius=8,
                )
            )
            
        page.controls = [
            navbar,
            ft.Text("Individual Project Timeline", size=26, weight="bold", color=PRIMARY_COLOR),
            ft.Text("Chronological index tracing explicit structural development contributions.", size=14, color=TEXT_LIGHT),
            ft.Divider(color=BORDER_COLOR),
            ft.Column(timeline_cards, spacing=15)
        ]
        page.update()

    # ===== 3. MATLAB HUB VIEW =====
    def show_matlab():
        current_dir = os.path.dirname(os.path.abspath(__file__))
        img_absolute_path = os.path.normpath(os.path.join(current_dir, "assets", "images", "matlab_proof.png"))

        def open_certificate_file(e):
            try:
                if os.path.exists(img_absolute_path):
                    os.startfile(img_absolute_path)
            except Exception as ex:
                print(f"Error launching file resource: {ex}")

        courses = [
            "MATLAB Onramp", "Simulink Onramp", "Machine Learning Onramp", 
            "Deep Learning Onramp", "Image Processing Onramp", "Signal Processing Onramp", 
            "Control Design Onramp", "Stateflow Onramp"
        ]

        if os.path.exists(img_absolute_path):
            certificate_element = ft.Image(
                src="images/matlab_proof.png",
                width=150,
                fit="contain",  
                border_radius=6,
            )
        else:
            certificate_element = ft.Container(
                content=ft.Text(
                    value=f"⚠️ Image file missing in asset folder structure at:\n{img_absolute_path}",
                    color="red",
                    weight="bold"
                ),
                padding=20
            )

        page.controls = [
            navbar,
            ft.Text(value="MATLAB Academic Achievement Hub", size=26, weight="bold", color=PRIMARY_COLOR),
            ft.Text(value="MathWorks learning curriculum track validations and credentials.", size=14, color=TEXT_LIGHT),
            ft.Divider(color=BORDER_COLOR),
            
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Text(value="CURRICULUM COMPLETION STATUS", size=11, weight="bold", color=TEXT_LIGHT),
                                ft.Text(value="8 / 8 Courses Verified", size=22, weight="bold", color=PRIMARY_COLOR),
                            ],
                            spacing=4,
                            expand=True
                        ),
                        ft.Row(
                            controls=[
                                ft.Text(value="100%", size=16, weight="bold", color="#10B981"),
                                ft.ProgressRing(value=1.0, width=36, height=36, color="#10B981", bgcolor="#E2E8F0"),
                            ],
                            spacing=10
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                ),
                padding=20,
                bgcolor="#F0FDF4", 
                border=ft.Border.all(1, "#DCFCE7"),
                border_radius=10,
            ),
            
            ft.Container(height=5),
            ft.Text(value="Credentials Track List", size=16, weight="bold", color=PRIMARY_COLOR),
            
            
            
            ft.Container(height=10),
            ft.Text(value="Primary Academic Credential Evidence", size=16, weight="bold", color=PRIMARY_COLOR),
            
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(value="MathWorks Certificate Verification Registry", size=13, weight="w500", color=TEXT_LIGHT),
                        certificate_element, 
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=12
                ),
                padding=24,
                bgcolor="#FFFFFF", 
                border=ft.Border.all(1, BORDER_COLOR),
                border_radius=12,
            ),
        ]
        page.update()

    # ===== 4. BLOG VIEW =====
    def show_blog():
        page.controls = [
            navbar,
            ft.Text("Technical Blog: Confidence in Concepts", size=26, weight="bold", color=PRIMARY_COLOR),
            ft.Text("Application of analytical structural mechanics equations.", size=14, color=TEXT_LIGHT),
            ft.Divider(color=BORDER_COLOR),
            
            ft.Container(
                content=ft.Column([
                    ft.Text("Structural Mechanics: Beam Deflection Models", size=18, weight="bold", color=PRIMARY_COLOR),
                    ft.Text("Context: Flexural Analysis under Uniform Distributed Loads (UDL)", size=12, color=TEXT_LIGHT),
                    ft.Divider(color=BORDER_COLOR),
                    ft.Text("The structural calculation model matrix evaluates member boundary limits cleanly.", size=14),
                ], spacing=12),
                padding=24,
                bgcolor=CARD_BG,
                border=ft.Border.all(1, BORDER_COLOR),
                border_radius=8,
            ),
        ]
        page.update()
    
    # ===== 5. GITHUB & EXECUTIVES VIEW =====
    def show_github():
        pr_logs = [
            ("PR #4 - MERGED", "Feature: Integrate Mineral Analysis Database Schema", 
             "Proposed a pull request to merge individual Firestore collection definitions tracking sample metadata, mineral hardness indexes, and elemental analysis data."),
            ("PR #2 - MERGED", "Security: Implement System Lockdown Logic for Unauthorized Roles", 
             "Developed and pushed branch handling administrative toggle settings. This code intercepts illicit read requests when lockdown mode is true.")
        ]
        
        pr_list_controls = []
        for status, title, summary in pr_logs:
            pr_list_controls.append(
                ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Container(ft.Text(status, size=11, color="white", weight="bold"), bgcolor="#10B981" if "MERGED" in status else "#3B82F6", padding=5, border_radius=4),
                            ft.Text(title, size=14, weight="bold", color=PRIMARY_COLOR),
                        ], spacing=10),
                        ft.Text(f"Summary: {summary}", size=13, color=TEXT_DARK),
                    ], spacing=6),
                    padding=15,
                    border=ft.Border.all(1, BORDER_COLOR),
                    border_radius=6,
                    bgcolor="#F8FAFC"
                )
            )

        page.controls = [
            navbar,
            ft.Text("GitHub Evidence & System Documentation", size=26, weight="bold", color=PRIMARY_COLOR),
            ft.Text("Verifiable version control tracking, branch contributions, and metallurgical problem impact analysis.", size=14, color=TEXT_LIGHT),
            ft.Divider(color=BORDER_COLOR),
            
            ft.Container(
                content=ft.Column([
                    ft.Text("Engineering Impact Summary", size=18, weight="bold", color=PRIMARY_COLOR),
                    ft.Text("Project Type: Metallurgy & Mineral Quality Assurance Application", size=12, color=TEXT_LIGHT, italic=True),
                    ft.Divider(color=BORDER_COLOR),
                    ft.Text(
                        "Problem Solved:\n"
                        "In mining and processing metallurgy operations, lab technicians require real-time validation of mineral assay parameters.\n\n"
                        "How My Code Solved It:\n"
                        "I engineered a decoupled analytical dashboard environment using Python/Flet and backend Firestore listeners. "
                        "By structuring specific state controls, I established an isolated 'Lab Technician Portal' that processes sample metrics cleanly.",
                        size=14, color=TEXT_DARK
                    ),
                ], spacing=10),
                padding=24,
                bgcolor=CARD_BG,
                border=ft.Border.all(1, BORDER_COLOR),
                border_radius=8,
            ),
            
            ft.Container(
                content=ft.Column([
                    ft.Text("Proposed Pull Request Logs (PRs)", size=18, weight="bold", color=PRIMARY_COLOR),
                    ft.Column(pr_list_controls, spacing=10)
                ], spacing=12),
                padding=24,
                bgcolor=CARD_BG,
                border=ft.Border.all(1, BORDER_COLOR),
                border_radius=8,
            ),
            
            ft.Container(
                content=ft.Column([
                    ft.Text("Verifiable Commit History Evidence", size=18, weight="bold", color=PRIMARY_COLOR),
                    ft.Image(
                        src="images/github_proof.png",  
                        width=550,
                        fit="contain",
                        border_radius=8,
                    ),
                ], horizontal_alignment="center", spacing=10),
                padding=24,
                bgcolor=CARD_BG,
                border=ft.Border.all(1, BORDER_COLOR),
                border_radius=8,
            ),
        ]
        page.update()
    
    # ===== INITIAL INITIALIZATION =====
    show_home()

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    assets_path = os.path.join(current_dir, "assets")
    ft.run(main, assets_dir=assets_path)
    ft.app(target=main, assets_dir=assets_path, view=ft.AppView.WEB_BROWSER)