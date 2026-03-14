import flet as ft

def main(page: ft.Page):
    page.title = "Engineering Web Portfolio"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = "adaptive"

    # --- Section 1: Project Timeline ---
    timeline_content = ft.Column([
        ft.Text("Weekly Project Log", size=30, weight="bold"),
        ft.Text("Week 1: Set up repository and initialized Flet structure."),
        ft.Text("Week 2: Developed the calculation engine for Civil Engineering."),
    ], visible=True)

    # --- Section 2: MATLAB Achievement Hub ---
    matlab_content = ft.Column([
        ft.Text("MATLAB Achievement Hub", size=30, weight="bold"),
        ft.Text("Proof of completion for 8 short self-paced courses."),
        # You will add your certificate images here later
    ], visible=False)

    # --- Section 3: Technical Blog ---
    blog_content = ft.Column([
        ft.Text("Technical Blog", size=30, weight="bold"),
        ft.Markdown(
            r"Total Cost = $\sum_{i=1}^{n} (Q_i \times P_i) + \text{Overheads}$",
            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
        )
    ], visible=False)

    # --- NEW Section 4: GitHub Evidence ---
    github_content = ft.Column([
        ft.Text("GitHub Evidence & Documentation", size=30, weight="bold"),
        ft.Text("Impact Summary:", weight="bold"),
        ft.Text(
            "I managed the structural analysis logic for the Civil Engineering module, "
            "ensuring that the load distribution calculations were accurate and efficient."
        ),
        ft.Text("Individual Commits:", weight="bold"),
        # Placeholder for your screenshot
        ft.Text("[Insert Commit Screenshot Here]", italic=True, color=ft.colors.GREY_700),
    ], visible=False)

    # --- Navigation Logic ---
    def navigate(e):
        # Hide all
        timeline_content.visible = False
        matlab_content.visible = False
        blog_content.visible = False
        github_content.visible = False
        
        # Show selected
        if e.control.text == "Timeline": timeline_content.visible = True
        elif e.control.text == "MATLAB": matlab_content.visible = True
        elif e.control.text == "Blog": blog_content.visible = True
        elif e.control.text == "GitHub": github_content.visible = True
        
        page.update()

    # Clean Navigation using the updated Button component
    nav_buttons = ft.Row([
        ft.FilledButton("Timeline", on_click=navigate),
        ft.FilledButton("MATLAB", on_click=navigate),
        ft.FilledButton("Blog", on_click=navigate),
        ft.FilledButton("GitHub", on_click=navigate),
    ], alignment=ft.MainAxisAlignment.CENTER)

    page.add(
        nav_buttons,
        ft.Divider(),
        timeline_content,
        matlab_content,
        blog_content,
        github_content
    )

if __name__ == "__main__":
    # Updated to 'run' to remove the DeprecationWarning
    ft.app(target=main)