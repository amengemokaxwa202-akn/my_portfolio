import logging  
import flet as ft
import flet_video as fv
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
                            width=250,
                            height=250,
                            fit="cover",
                            border_radius=150,
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
                            ft.Text("7 Courses", size=22, weight="bold", color=PRIMARY_COLOR),
                            ft.Text("View Certificates →", size=11, color=SECONDARY_COLOR, weight="w500"),
                        ], spacing=4),
                        padding=30,
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
                        padding=30,
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
                        padding=30,
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

        if os.path.exists(img_absolute_path) or os.getenv("PORT"):  
            certificate_element = ft.Image(
                src="images/matlab_proof.png",
                width=500,
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
                                ft.Text(value="7 / 7 Courses Verified", size=22, weight="bold", color=PRIMARY_COLOR),
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
            ft.Text(value="Primary Academic Credential Evidence", size=16, weight="bold", color=PRIMARY_COLOR),
            
            ft.Row(
                controls=[
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
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
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
            
            # UPDATED: Replaced legacy HTML5 view with native flet_video player implementation
            ft.Container(
                content=ft.Column([
                    ft.Text("System Walkthrough Integration & Technical Video Demonstration", size=18, weight="bold", color=PRIMARY_COLOR),
                    ft.Text("Video proof showing dynamic operational layouts and frontend route parsing.", size=12, color=TEXT_LIGHT),
                    ft.Divider(color=BORDER_COLOR),
                    
                    fv.Video(
                        playlist=[
                            fv.VideoMedia("videos/demo.mp4")
                        ],
                        expand=True
                    ),
                ], horizontal_alignment="center", spacing=15),
                padding=24,
                bgcolor=CARD_BG,
                border=ft.Border.all(1, BORDER_COLOR),
                border_radius=8,
                height=400
            ),
        ]
        page.update()
    
    # ===== 5. GITHUB VIEW =====
    def show_github():
        pr_logs = [
            ("COMMIT", "Full EM-Lab code with Login and Signup screens", "Initial structural push translating the authentication portal layouts for user entry views."),
            ("COMMIT", "Dashboard converted from general dashboard to dynamic dashboard that pro…", "Converted layout states from static elements to responsive data hooks tracking active states."),
            ("COMMIT", "feat: add role-based dashboard and profile screen", "Implements dynamic visibility toggles checking authorization parameters to render custom lab views."),
            ("COMMIT", "feat: implement Firebase Auth and Firestore user registration", "Wires up backend connection strings to pass user payloads safely over SSL into target cloud collections."),
            ("COMMIT", "feat: implement multi-user registration flow for Admin dashboard", "Allows administrative level roles to provision secondary workspace credentials efficiently."),
            ("COMMIT", "style: update container background color to #1A1A2E", "Applied updated darkness layout values matching the team's visual style specification sheets."),
            ("COMMIT", "final: pre-pull commit of unified app structure", "Saves local workspace parameters before triggering remote repository sync operations."),
            ("COMMIT", "feat: implement auth persistence with AsyncStorage and session listener", "Tracks user token lifecycles to prevent unexpected app logouts between routine application restarts."),
            ("COMMIT", "refactor: consolidate project to root App.js and remove old src structur…", "Consolidated project directories down into root components. NOTE: This structure was an initial mistake; bundling everything into App.js created scalability bottlenecks, forcing us to later break it down back into modular files."),
            ("COMMIT", "feat: add password reset functionality to user profile", "Adds self-service account recovery triggers for automated credential reset dispatches."),
            ("COMMIT", "fix: implement safe firebase initialization and forgot password logic", "Patches race-conditions preventing backend context initialization at execution load limits."),
            ("COMMIT", "fix: stabilize auth persistence and resolve redirect loop", "Trims routing loop logic flags that were misfiring inside state checking modules."),
            ("COMMIT", "chore: initialize firebase config and implement isReady loading state", "Configures network endpoints and anchors application execution states until initial handshakes pass."),
            ("COMMIT", "feat: finalize auth architecture and registration workflows", "Locks in secure user authentication boundaries and structural sign-up routes."),
            ("COMMIT", "feat: staff registration system is fully operational and authenticated", "Finalizes individual sign-up security criteria for live laboratory staff verification."),
            ("COMMIT", "fix: migrate ViewSamplesScreen to sampleCard styles, add sampleSource an…", "Standardizes cross-component layout constraints to use shared UI card dictionaries seamlessly."),
            ("COMMIT", "Bug Fix — displayId wins fallback, should use sampleId first", "Corrects an evaluation oversight by forcing the key parser to fetch unique sample IDs before string backups."),
            ("COMMIT", "Bug Fix — wrong variable name, sample → selectedSample", "Corrects a scoping variable assignment typo that was breaking rendering properties inside sub-panels."),
            ("COMMIT", "fix: retain samples in assay history after furnace operator begins melt …", "Patches state tracking matrices to lock assay data references securely even when processing tasks begin downstream.")
        ]
        
        pr_list_controls = []
        for status, title, summary in pr_logs:
            pr_list_controls.append(
                ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Container(ft.Text(status, size=11, color="white", weight="bold"), bgcolor="#3B82F6", padding=5, border_radius=4),
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
                ], horizontal_alignment="center", spacing=15),
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
    server_port = int(os.getenv("PORT", 8000))
    app_host = "0.0.0.0" if os.getenv("PORT") else "127.0.0.1"
    
    ft.run(
        main, 
        assets_dir="assets", 
        view=ft.AppView.WEB_BROWSER,
        host=app_host,
        port=server_port
    )