from frontend.components.website.hero import hero_section
from frontend.components.website.about import about_section
from frontend.components.website.services import services_section
from frontend.components.website.faq import faq_section



def render_section(section):

    section_type = section.get("type")

    if section_type == "hero":
        return hero_section(section)

    if section_type == "about":
        return about_section(section)

    if section_type == "services":
        return services_section(section)

    if section_type == "faq":
        return faq_section(section)