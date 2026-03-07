import re

filepath = r'c:\Users\ACER\OneDrive\Desktop\rushi portfolio\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

header_old = '<h2 class=\"section__title reveal\">Projects</h2>\n\n      <div class=\"projects__grid\">'
header_new = '''<h2 class=\"section__title reveal\">Projects From My Development Track</h2>\n      <p class=\"reveal\" style=\"text-align: center; margin-top: -30px; margin-bottom: 50px; font-size: 1.1rem; color: var(--text-muted);\">\n        Every project is a new lap where I learn, experiment, and push my limits as a developer.\n      </p>\n\n      <div class=\"track-timeline reveal\">\n        <div class=\"track-line\">\n          <div class=\"track-progress\" id=\"trackProgress\"></div>\n        </div>\n        <div class=\"projects__grid\">'''

content = content.replace(header_old, header_new)

content = content.replace('<div class=\"project-card reveal\">', '<div class=\"checkpoint\"><div class=\"checkpoint-dot\"></div><div class=\"project-card reveal\">')

content = re.sub(r'(<div class=\"project-card__actions\">[\s\S]*?</div>\s*</div>\s*</div>)', r'\1\n        </div>', content)

grid_end_old = '      </div>\n    </div>\n  </section>'
grid_end_new = '        </div>\n      </div>\n    </div>\n  </section>'
content = content.replace(grid_end_old, grid_end_new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print('Done!')
