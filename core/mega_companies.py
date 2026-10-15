"""Massive curated company list — Kenyan tech & finance + MNCs with Kenya offices + Global remote-friendly.
Every company here has an engineering/software team and has been around 5+ years.
Organized by category for easy management.

NOTE: employee_count and founded_year are approximate. Verify before relying on them."""


# ── Kenyan Tech Giants & Unicorns ──────────────────────────────

KENYAN_TECH = [
    # Telecom & Digital Services
    {"name": "Safaricom", "domain": "safaricom.co.ke", "tags": "telecom,fintech,mpesa,kenya-hq", "employee_count": "6000+", "founded_year": 1997},
    {"name": "Airtel Kenya", "domain": "airtel.co.ke", "tags": "telecom,kenya-hq", "employee_count": "1000+", "founded_year": 2000},
    {"name": "Telkom Kenya", "domain": "telkom.co.ke", "tags": "telecom,kenya-hq", "employee_count": "1000+", "founded_year": 1999},
    {"name": "Craft Silicon", "domain": "craftsilicon.com", "tags": "it-services,fintech,software,kenya-hq", "employee_count": "1000+", "founded_year": 1997},
    {"name": "Kenya Power", "domain": "kplc.co.ke", "tags": "utility,energy,kenya-hq", "employee_count": "10000+", "founded_year": 1922},

    # Kenyan Fintech & Payments
    {"name": "M-KOPA", "domain": "m-kopa.com", "tags": "fintech,asset-financing,iot,kenya-hq", "employee_count": "3000+", "founded_year": 2011},
    {"name": "Africa's Talking", "domain": "africastalking.com", "tags": "api,communications,fintech,kenya-hq", "employee_count": "200+", "founded_year": 2010},
    {"name": "Pesapal", "domain": "pesapal.com", "tags": "fintech,payments,kenya-hq", "employee_count": "200+", "founded_year": 2009},
    {"name": "Tala", "domain": "tala.co", "tags": "fintech,lending,kenya-office", "employee_count": "500+", "founded_year": 2011},
    {"name": "Branch", "domain": "branch.co", "tags": "fintech,lending,kenya-office", "employee_count": "500+", "founded_year": 2015},
    {"name": "Kopo Kopo", "domain": "kopokopo.com", "tags": "fintech,payments,smb,kenya-hq", "employee_count": "100+", "founded_year": 2011},
    {"name": "Lipa Later", "domain": "lipalater.com", "tags": "fintech,bnpl,kenya-hq", "employee_count": "100+", "founded_year": 2017},
    {"name": "Pezesha", "domain": "pezesha.com", "tags": "fintech,lending,kenya-hq", "employee_count": "50+", "founded_year": 2016},

    # Kenyan Banks (large tech/engineering teams)
    {"name": "Equity Group", "domain": "equitygroupholdings.com", "tags": "banking,fintech,kenya-hq", "employee_count": "15000+", "founded_year": 1984},
    {"name": "KCB Group", "domain": "kcbgroup.com", "tags": "banking,fintech,kenya-hq", "employee_count": "8000+", "founded_year": 1896},
    {"name": "Co-operative Bank of Kenya", "domain": "co-opbank.co.ke", "tags": "banking,kenya-hq", "employee_count": "6000+", "founded_year": 1965},
    {"name": "NCBA Group", "domain": "ncbagroup.com", "tags": "banking,fintech,kenya-hq", "employee_count": "3000+", "founded_year": 1962},
    {"name": "Absa Bank Kenya", "domain": "absabank.co.ke", "tags": "banking,kenya-office", "employee_count": "3000+", "founded_year": 1916},
    {"name": "Stanbic Bank Kenya", "domain": "stanbicbank.co.ke", "tags": "banking,kenya-office", "employee_count": "1500+", "founded_year": 1995},
    {"name": "Standard Chartered Kenya", "domain": "sc.com", "tags": "banking,kenya-office", "employee_count": "1500+", "founded_year": 1911},
    {"name": "I&M Bank", "domain": "imbank.com", "tags": "banking,kenya-hq", "employee_count": "1500+", "founded_year": 1974},
    {"name": "Diamond Trust Bank", "domain": "dtbafrica.com", "tags": "banking,kenya-hq", "employee_count": "2000+", "founded_year": 1946},
    {"name": "Family Bank", "domain": "familybank.co.ke", "tags": "banking,kenya-hq", "employee_count": "1500+", "founded_year": 1984},
    {"name": "Britam", "domain": "britam.com", "tags": "insurance,fintech,kenya-hq", "employee_count": "1000+", "founded_year": 1965},
    {"name": "Jubilee Insurance", "domain": "jubileeinsurance.com", "tags": "insurance,kenya-hq", "employee_count": "1000+", "founded_year": 1937},

    # Kenyan E-commerce / Marketplace / Logistics
    {"name": "Jumia Kenya", "domain": "jumia.co.ke", "tags": "ecommerce,marketplace,kenya-office", "employee_count": "1000+", "founded_year": 2012},
    {"name": "Kilimall", "domain": "kilimall.co.ke", "tags": "ecommerce,marketplace,kenya-office", "employee_count": "200+", "founded_year": 2014},
    {"name": "Twiga Foods", "domain": "twigafoods.com", "tags": "agritech,b2b,marketplace,kenya-hq", "employee_count": "500+", "founded_year": 2013},
    {"name": "Wasoko", "domain": "wasoko.com", "tags": "ecommerce,b2b,retail,kenya-hq", "employee_count": "500+", "founded_year": 2016},
    {"name": "Apollo Agriculture", "domain": "apolloagriculture.com", "tags": "agritech,fintech,kenya-hq", "employee_count": "500+", "founded_year": 2016},
    {"name": "Little", "domain": "little.bz", "tags": "mobility,ride-hailing,kenya-hq", "employee_count": "200+", "founded_year": 2016},

    # Kenyan Edtech / Healthtech / Other
    {"name": "Moringa School", "domain": "moringaschool.com", "tags": "edtech,bootcamp,kenya-hq", "employee_count": "200+", "founded_year": 2014},
    {"name": "Eneza Education", "domain": "enezaeducation.com", "tags": "edtech,mobile,kenya-hq", "employee_count": "100+", "founded_year": 2012},
    {"name": "Ushahidi", "domain": "ushahidi.com", "tags": "civic-tech,open-source,kenya-hq", "employee_count": "50+", "founded_year": 2008},
    {"name": "Ona", "domain": "ona.io", "tags": "data,mobile-data-collection,kenya-office", "employee_count": "100+", "founded_year": 2013},
    {"name": "Sun King", "domain": "sunking.com", "tags": "cleantech,iot,fintech,kenya-office", "employee_count": "3000+", "founded_year": 2006},
    {"name": "BasiGo", "domain": "basigo.com", "tags": "cleantech,mobility,kenya-hq", "employee_count": "100+", "founded_year": 2021},
]

# ── Pan-African Tech with Nairobi Presence ─────────────────────

PAN_AFRICAN = [
    {"name": "Cellulant", "domain": "cellulant.io", "tags": "fintech,payments,africa-hq,kenya-office", "employee_count": "500+", "founded_year": 2004},
    {"name": "Flutterwave", "domain": "flutterwave.com", "tags": "fintech,payments,africa-hq,kenya-office", "employee_count": "1000+", "founded_year": 2016},
    {"name": "Paystack", "domain": "paystack.com", "tags": "fintech,payments,africa-hq,kenya-office", "employee_count": "300+", "founded_year": 2015},
    {"name": "Chipper Cash", "domain": "chippercash.com", "tags": "fintech,payments,africa-hq,kenya-office", "employee_count": "300+", "founded_year": 2018},
    {"name": "Interswitch", "domain": "interswitchgroup.com", "tags": "fintech,payments,africa-hq,kenya-office", "employee_count": "1000+", "founded_year": 2002},
    {"name": "Jumia", "domain": "jumia.com", "tags": "ecommerce,africa-hq,kenya-office", "employee_count": "2000+", "founded_year": 2012},
    {"name": "Liquid Intelligent Technologies", "domain": "liquid.tech", "tags": "telecom,cloud,africa-hq,kenya-office", "employee_count": "3000+", "founded_year": 2003},
]

# ── MNCs with Large Kenya / East Africa Engineering Centers ────

MNCS_KENYA = [
    {"name": "Google Kenya", "domain": "google.com", "tags": "big-tech,kenya-office", "employee_count": "100000+", "founded_year": 1998},
    {"name": "Microsoft Kenya", "domain": "microsoft.com", "tags": "big-tech,kenya-office", "employee_count": "200000+", "founded_year": 1975},
    {"name": "Amazon Web Services Kenya", "domain": "aws.amazon.com", "tags": "big-tech,cloud,kenya-office", "employee_count": "100000+", "founded_year": 2006},
    {"name": "IBM Research Africa", "domain": "ibm.com", "tags": "enterprise,research,kenya-office", "employee_count": "100000+", "founded_year": 1911},
    {"name": "Oracle Kenya", "domain": "oracle.com", "tags": "enterprise,database,kenya-office", "employee_count": "40000+", "founded_year": 1977},
    {"name": "SAP Kenya", "domain": "sap.com", "tags": "enterprise,erp,kenya-office", "employee_count": "15000+", "founded_year": 1972},
    {"name": "Cisco Kenya", "domain": "cisco.com", "tags": "networking,kenya-office", "employee_count": "12000+", "founded_year": 1984},
    {"name": "Huawei Kenya", "domain": "huawei.com", "tags": "telecom,electronics,kenya-office", "employee_count": "5000+", "founded_year": 1987},
    {"name": "Ericsson Kenya", "domain": "ericsson.com", "tags": "telecom,networking,kenya-office", "employee_count": "1000+", "founded_year": 1876},
    {"name": "Nokia Kenya", "domain": "nokia.com", "tags": "telecom,networking,kenya-office", "employee_count": "1000+", "founded_year": 1865},
    {"name": "Visa Kenya", "domain": "visa.com", "tags": "fintech,payments,kenya-office", "employee_count": "4000+", "founded_year": 1958},
    {"name": "Mastercard Kenya", "domain": "mastercard.com", "tags": "fintech,payments,kenya-office", "employee_count": "3000+", "founded_year": 1966},
    {"name": "Uber Kenya", "domain": "uber.com", "tags": "mobility,kenya-office", "employee_count": "5000+", "founded_year": 2009},
    {"name": "Bolt Kenya", "domain": "bolt.eu", "tags": "mobility,ride-hailing,kenya-office", "employee_count": "3000+", "founded_year": 2013},
    {"name": "Accenture Kenya", "domain": "accenture.com", "tags": "consulting,it-services,kenya-office", "employee_count": "300000+", "founded_year": 1989},
    {"name": "Deloitte Kenya", "domain": "deloitte.com", "tags": "consulting,kenya-office", "employee_count": "50000+", "founded_year": 1845},
    {"name": "PwC Kenya", "domain": "pwc.com", "tags": "consulting,kenya-office", "employee_count": "50000+", "founded_year": 1998},
    {"name": "EY Kenya", "domain": "ey.com", "tags": "consulting,kenya-office", "employee_count": "40000+", "founded_year": 1989},
    {"name": "KPMG Kenya", "domain": "kpmg.com", "tags": "consulting,kenya-office", "employee_count": "30000+", "founded_year": 1987},
    {"name": "Cognizant Kenya", "domain": "cognizant.com", "tags": "it-services,kenya-office", "employee_count": "250000+", "founded_year": 1994},
    {"name": "Dimension Data Kenya", "domain": "dimensiondata.com", "tags": "it-services,cloud,kenya-office", "employee_count": "10000+", "founded_year": 1983},
    {"name": "Citibank Kenya", "domain": "citigroup.com", "tags": "finance,kenya-office", "employee_count": "5000+", "founded_year": 1812},
    {"name": "Equinix Kenya", "domain": "equinix.com", "tags": "infrastructure,data-centers,kenya-office", "employee_count": "10000+", "founded_year": 1998},
]

# ── Global Remote-Friendly Companies (hire from Kenya / Africa) ─

GLOBAL_REMOTE = [
    {"name": "GitLab", "domain": "gitlab.com", "tags": "devops,open-source,remote-first", "employee_count": "2000+", "founded_year": 2014},
    {"name": "Automattic", "domain": "automattic.com", "tags": "wordpress,open-source,remote-first", "employee_count": "2000+", "founded_year": 2005},
    {"name": "Canonical", "domain": "canonical.com", "tags": "ubuntu,open-source,remote-first", "employee_count": "1000+", "founded_year": 2004},
    {"name": "Zapier", "domain": "zapier.com", "tags": "automation,saas,remote-first", "employee_count": "800+", "founded_year": 2011},
    {"name": "Buffer", "domain": "buffer.com", "tags": "social,saas,remote-first", "employee_count": "100+", "founded_year": 2010},
    {"name": "Toggl", "domain": "toggl.com", "tags": "productivity,saas,remote-first", "employee_count": "200+", "founded_year": 2006},
    {"name": "Doist", "domain": "doist.com", "tags": "productivity,saas,remote-first", "employee_count": "100+", "founded_year": 2007},
    {"name": "Hotjar", "domain": "hotjar.com", "tags": "analytics,saas,remote-first", "employee_count": "500+", "founded_year": 2014},
    {"name": "Deel", "domain": "deel.com", "tags": "hr,payroll,remote-first", "employee_count": "3000+", "founded_year": 2019},
    {"name": "Remote.com", "domain": "remote.com", "tags": "hr,remote-first", "employee_count": "1000+", "founded_year": 2019},
    {"name": "Toptal", "domain": "toptal.com", "tags": "marketplace,talent,remote-first", "employee_count": "1000+", "founded_year": 2010},
    {"name": "Turing", "domain": "turing.com", "tags": "marketplace,talent,remote-first", "employee_count": "1000+", "founded_year": 2018},
    {"name": "Andela", "domain": "andela.com", "tags": "marketplace,talent,remote-first,africa-focused", "employee_count": "500+", "founded_year": 2014},
    {"name": "Mattermost", "domain": "mattermost.com", "tags": "chat,open-source,remote-first", "employee_count": "300+", "founded_year": 2016},
    {"name": "Supabase", "domain": "supabase.com", "tags": "database,open-source,remote-first", "employee_count": "200+", "founded_year": 2020},
    {"name": "Linear", "domain": "linear.app", "tags": "project-management,saas,remote-first", "employee_count": "100+", "founded_year": 2019},
    {"name": "Cal.com", "domain": "cal.com", "tags": "scheduling,open-source,remote-first", "employee_count": "100+", "founded_year": 2021},
    {"name": "Airbyte", "domain": "airbyte.com", "tags": "data,etl,open-source,remote-first", "employee_count": "200+", "founded_year": 2020},
    {"name": "Grafana Labs", "domain": "grafana.com", "tags": "monitoring,open-source,remote-first", "employee_count": "1000+", "founded_year": 2014},
    {"name": "Elastic", "domain": "elastic.co", "tags": "search,open-source,remote-first", "employee_count": "3000+", "founded_year": 2012},
    {"name": "Wikimedia Foundation", "domain": "wikimedia.org", "tags": "non-profit,open-source,remote-first", "employee_count": "500+", "founded_year": 2003},
    {"name": "Mozilla", "domain": "mozilla.org", "tags": "browser,open-source,remote-first", "employee_count": "1000+", "founded_year": 2003},
    {"name": "Red Hat", "domain": "redhat.com", "tags": "linux,open-source,remote-first", "employee_count": "20000+", "founded_year": 1993},
    {"name": "SUSE", "domain": "suse.com", "tags": "linux,open-source,remote-first", "employee_count": "2000+", "founded_year": 1992},
    {"name": "DigitalOcean", "domain": "digitalocean.com", "tags": "cloud,remote-first", "employee_count": "1000+", "founded_year": 2011},
    {"name": "Cloudflare", "domain": "cloudflare.com", "tags": "infrastructure,security,cdn", "employee_count": "3000+", "founded_year": 2009},
    {"name": "Hashicorp", "domain": "hashicorp.com", "tags": "devops,infrastructure,open-source", "employee_count": "2000+", "founded_year": 2012},
    {"name": "Kong", "domain": "konghq.com", "tags": "api-gateway,open-source", "employee_count": "500+", "founded_year": 2009},
    {"name": "Snyk", "domain": "snyk.io", "tags": "security,devtools", "employee_count": "1000+", "founded_year": 2015},
    {"name": "Docker", "domain": "docker.com", "tags": "containers,devtools", "employee_count": "500+", "founded_year": 2008},
    {"name": "CircleCI", "domain": "circleci.com", "tags": "ci-cd,devops", "employee_count": "500+", "founded_year": 2011},
    {"name": "PagerDuty", "domain": "pagerduty.com", "tags": "incident-mgmt,saas", "employee_count": "1000+", "founded_year": 2009},
    {"name": "Datadog", "domain": "datadoghq.com", "tags": "monitoring,observability", "employee_count": "5000+", "founded_year": 2010},
    {"name": "New Relic", "domain": "newrelic.com", "tags": "monitoring,observability", "employee_count": "2000+", "founded_year": 2008},
    {"name": "Sentry", "domain": "sentry.io", "tags": "error-tracking,monitoring", "employee_count": "500+", "founded_year": 2012},
    {"name": "LaunchDarkly", "domain": "launchdarkly.com", "tags": "feature-flags,devtools", "employee_count": "500+", "founded_year": 2014},
    {"name": "Vercel", "domain": "vercel.com", "tags": "cloud,frontend,devtools", "employee_count": "500+", "founded_year": 2015},
    {"name": "Netlify", "domain": "netlify.com", "tags": "cloud,jamstack", "employee_count": "300+", "founded_year": 2014},
    {"name": "Render", "domain": "render.com", "tags": "cloud,paas", "employee_count": "200+", "founded_year": 2018},
    {"name": "Fly.io", "domain": "fly.io", "tags": "cloud,edge", "employee_count": "100+", "founded_year": 2017},
    {"name": "Temporal", "domain": "temporal.io", "tags": "workflow,orchestration", "employee_count": "200+", "founded_year": 2019},
    {"name": "Cockroach Labs", "domain": "cockroachlabs.com", "tags": "database,distributed", "employee_count": "500+", "founded_year": 2015},
    {"name": "PlanetScale", "domain": "planetscale.com", "tags": "database,mysql", "employee_count": "200+", "founded_year": 2018},
    {"name": "Neon", "domain": "neon.tech", "tags": "database,postgres,serverless", "employee_count": "200+", "founded_year": 2021},
    {"name": "Retool", "domain": "retool.com", "tags": "internal-tools,low-code", "employee_count": "500+", "founded_year": 2017},
    {"name": "Webflow", "domain": "webflow.com", "tags": "no-code,web-design", "employee_count": "1000+", "founded_year": 2013},
    {"name": "Figma", "domain": "figma.com", "tags": "design,saas", "employee_count": "1000+", "founded_year": 2012},
    {"name": "Notion", "domain": "notion.so", "tags": "productivity,saas", "employee_count": "500+", "founded_year": 2016},
    {"name": "Stripe", "domain": "stripe.com", "tags": "fintech,payments,api", "employee_count": "5000+", "founded_year": 2010},
    {"name": "Plaid", "domain": "plaid.com", "tags": "fintech,api,banking", "employee_count": "1000+", "founded_year": 2013},
    {"name": "Brex", "domain": "brex.com", "tags": "fintech,corporate-cards", "employee_count": "1000+", "founded_year": 2017},
    {"name": "Ramp", "domain": "ramp.com", "tags": "fintech,expense", "employee_count": "500+", "founded_year": 2019},
    {"name": "Coinbase", "domain": "coinbase.com", "tags": "crypto,exchange", "employee_count": "3000+", "founded_year": 2012},
    {"name": "Ripple", "domain": "ripple.com", "tags": "crypto,payments", "employee_count": "500+", "founded_year": 2012},
]


def get_all_mega_companies() -> list[dict]:
    """Return all companies with kenya_friendly and id set."""
    from core.models import Company
    result = []
    seen = set()

    for category, companies, default_kenya in [
        ("kenyan-tech", KENYAN_TECH, "yes"),
        ("pan-african", PAN_AFRICAN, "yes"),
        ("mncs-kenya", MNCS_KENYA, "yes"),
        ("global-remote", GLOBAL_REMOTE, "maybe"),
    ]:
        for c in companies:
            company_id = Company.make_id(c["name"])
            if company_id in seen:
                continue
            seen.add(company_id)

            result.append({
                "id": company_id,
                "name": c["name"],
                "domain": c.get("domain", ""),
                "careers_url": "",
                "ats_platform": "unknown",
                "ats_slug": "",
                "founded_year": c.get("founded_year", 0),
                "employee_count": c.get("employee_count", ""),
                "tags": c.get("tags", ""),
                "kenya_friendly": c.get("kenya_friendly", default_kenya),
                "last_crawled": "",
                "crawl_status": "paused",  # paused until ATS detected
                "notes": category,
            })

    return result
