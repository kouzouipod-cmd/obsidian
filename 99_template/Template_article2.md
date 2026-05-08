---
citekey: "{{citekey}}"
dateread: '{{importDate | format("YYYY-MM-DD")}}'
read: false
---
 > [!Data]
> **PDF** {%- for attachment in attachments | filterby("path", "endswith", ".pdf") %}
> [{{attachment.title}}](file://{{attachment.path | replace(" ", "%20")}}) {%- endfor -%}.
> **Link**
> {%- if url %}[{{title}}]({{url}}){%- endif %}


# 1 AI要約








>[!Info]
{% for type, creators in creators | groupby("creatorType") -%}
{%- for creator in creators -%}
> **{{"First" if loop.first}}{{type | capitalize}}**::
{%- if creator.name %} {{creator.name}}  
{%- else %} {{creator.lastName}}, {{creator.firstName}}{%- endif %}  {% endfor %}{%- endfor %}
> **Title**: {{title}}
> **Year**: {{date | format("YYYY")}}
> **Citekey**: {{citekey}} {%- if itemType %}
> **itemType**: {{itemType}}{%- endif %}{%- if itemType == "journalArticle" %}
> **Journal**: *{{publicationTitle}}* {%- endif %}{%- if volume %}
> **Volume**: {{volume}} {%- endif %}{%- if issue %}
> **Issue**: {{issue}}{%- endif %}

> [!Abstract]
{%- if abstractNote %}
{%- for line in abstractNote.split('\n') %}
> {{line}}
{%- endfor %}

{% endif -%}

# 4 Main Text
