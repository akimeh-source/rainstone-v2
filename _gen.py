#!/usr/bin/env python
"""Generate all inner pages for Rainstone Money website using buy-to-let-mortgages.html as template."""
import re

with open("buy-to-let-mortgages.html", encoding="utf-8") as f:
    TMPL = f.read()

def hero_html(label, h1a, h1b, subtitle, tab="tab-personal"):
    return f'''<section class="hero hero-split {tab}" id="hero" style="min-height: 60vh;">
        <div class="hero-panel-left">
            <div class="hero-grain"></div>
            <div class="hero-diagonal-accent"></div>
            <div class="hero-text-wrap">
                <div class="hero-gold-line hero-anim" style="--delay:0ms"></div>
                <div class="hero-label hero-anim" style="--delay:100ms">{label}</div>
                <h1>
                    <span class="hero-line hero-anim" style="--delay:200ms">{h1a}</span>
                    <span class="hero-line hero-anim" style="--delay:350ms">{h1b}</span>
                </h1>
                <p class="hero-subtitle hero-anim" style="--delay:500ms">{subtitle}</p>
                <div class="hero-btns hero-anim" style="--delay:650ms">
                    <a href="#contact" class="btn btn-secondary">Free Consultation <i class="fas fa-arrow-right"></i></a>
                </div>
            </div>
        </div>
        <div class="hero-panel-right">
            <div class="hero-panel-img hero-img-personal"></div>
        </div>
    </section>'''

def scard(icon, title, tag, desc):
    return f'''                <div class="service-card">
                    <div class="service-icon"><i class="fas fa-{icon}"></i></div>
                    <h4>{title}</h4>
                    <p class="service-tag">{tag}</p>
                    <p>{desc}</p>
                </div>'''

def vcard(icon, title, desc):
    return f'''                <div class="value-card">
                    <div class="value-icon"><i class="fas fa-{icon}"></i></div>
                    <h4>{title}</h4>
                    <p>{desc}</p>
                </div>'''

def solutions_html(label, title_main, title_accent, h3, paras, cards, values, cta_text, btn_text="Get Expert Advice", tab="tab-personal"):
    paras_html = "\n".join(f"                    <p>{p}</p>" for p in paras)
    cards_html = "\n".join(cards)
    values_html = "\n".join(values)
    return f'''<section class="solutions-section {tab}">
        <div class="container">
            <div class="section-label" data-animate="fade-up">{label}</div>
            <h2 class="section-title" data-animate="fade-up">{title_main} <span class="text-accent">{title_accent}</span></h2>

            <div class="solutions-grid">
                <div class="solutions-content" data-animate="fade-right">
                    <h3>{h3}</h3>
{paras_html}
                    <a href="#contact" class="btn btn-primary">{btn_text} <i class="fas fa-arrow-right"></i></a>
                </div>
                <div class="solutions-image" data-animate="fade-left">
                    <div class="image-placeholder personal-img"></div>
                </div>
            </div>

            <div class="service-cards" data-animate="fade-up">
{cards_html}
            </div>

            <div class="values-row" data-animate="fade-up">
{values_html}
            </div>

            <div class="section-cta" data-animate="fade-up">
                <a href="#contact" class="btn btn-outline">{cta_text} <i class="fas fa-arrow-right"></i></a>
            </div>
        </div>
    </section>'''

def make_page(fn, title, meta, hero, sol, contact_sub="Connect with our experts for a free consultation and tailored advice.", mode="personal"):
    page = TMPL
    page = page.replace("Buy-to-Let Mortgages | Rainstone Money", f"{title} | Rainstone Money")
    page = page.replace(
        "Expert buy-to-let mortgage advice from Rainstone Money. Award-winning BTL specialists helping landlords and property investors secure the best rates.",
        meta
    )
    page = re.sub(r'<section class="hero hero-split.*?</section>', hero, page, flags=re.DOTALL)
    page = re.sub(r'<section class="solutions-section.*?</section>', sol, page, flags=re.DOTALL)
    page = page.replace(
        "Connect with our BTL experts for a free consultation and tailored advice.",
        contact_sub
    )
    # Set correct data-mode and active tab for commercial pages
    if mode == "commercial":
        page = page.replace('data-mode="personal"', 'data-mode="commercial"')
        page = page.replace(
            '<button class="mode-tab active" data-tab="personal">Personal</button>\n                <button class="mode-tab" data-tab="commercial">Commercial</button>',
            '<button class="mode-tab" data-tab="personal">Personal</button>\n                <button class="mode-tab active" data-tab="commercial">Commercial</button>'
        )
    with open(fn, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"  Created: {fn}")

# ============================================================
# PAGE DEFINITIONS
# ============================================================

print("Generating Rainstone Money pages...\n")

# 1. FLEXIBLE MORTGAGES
make_page("flexible-mortgage.html", "Flexible Mortgages",
    "Flexible mortgage solutions from Rainstone Money. Customise your repayments, make overpayments, and adapt your mortgage to your lifestyle.",
    hero_html("Award-Winning Mortgage Brokers",
        'Flexible <em class="text-gold-italic">Mortgages</em>',
        "Tailored to You",
        'Customisable repayments <span class="gold-dot">&middot;</span> Overpayment options <span class="gold-dot">&middot;</span> Adapt to your lifestyle'),
    solutions_html("FLEXIBLE MORTGAGES", "Mortgages That Adapt to", "Your Life",
        "Flexible Mortgage Solutions",
        [
            "Choosing the right mortgage for your specific circumstances is a pivotal decision. With flexible mortgages, you have options like changing interest rates, customising repayment plans, and making extra payments when it suits you.",
            "At Rainstone Money, we understand that life changes and your mortgage should be able to change with it. Whether you need payment holidays, the ability to overpay, or want to draw down funds when needed, our flexible mortgage solutions are designed around you.",
            "Our expert advisors will assess your financial situation and match you with lenders who offer the flexibility you need, ensuring you get a mortgage that truly works for your lifestyle."
        ],
        [
            scard("sliders", "Payment Flexibility", "Overpay or underpay", "Make overpayments when you can or take payment holidays when you need to. Flexible mortgages give you control over how and when you pay."),
            scard("percent", "Competitive Rates", "Best deals available", "Access exclusive rates from our panel of lenders. We negotiate on your behalf to secure the most competitive flexible mortgage deals on the market."),
            scard("user-check", "First-Time Buyers", "Your first step", "First-time buyer? We make the process simple with expert guidance from application to completion, helping you onto the property ladder with confidence.")
        ],
        [
            vcard("handshake", "Whole Market Access", "We search across the entire mortgage market to find flexible products that match your exact requirements and financial goals."),
            vcard("clock", "Fast Turnaround", "Our efficient process means you get a decision quickly, with most applications progressed within 48 hours of submission."),
            vcard("shield-halved", "Expert Guidance", "Our qualified advisors guide you through every option, explaining the benefits and considerations of each flexible mortgage product."),
            vcard("chart-line", "Ongoing Support", "Your relationship with us doesn't end at completion. We proactively review your mortgage to ensure it continues to work for you.")
        ],
        "Start Your Mortgage Journey",
        "Find Your Perfect Mortgage"),
    "Connect with our mortgage experts for a free consultation and personalised advice."
)

# 2. REMORTGAGING
make_page("remortgaging.html", "Remortgaging",
    "Expert remortgaging advice from Rainstone Money. Switch to a better deal, release equity, or consolidate debt with our award-winning brokers.",
    hero_html("Save Money, Switch Smarter",
        'Remortgaging <em class="text-gold-italic">Experts</em>',
        "Switch &amp; Save",
        'Better rates <span class="gold-dot">&middot;</span> Equity release options <span class="gold-dot">&middot;</span> Debt consolidation'),
    solutions_html("REMORTGAGING", "Time to Switch to a", "Better Deal?",
        "Expert Remortgaging Advice",
        [
            "Exploring different mortgage deals is crucial to finding one that suits your goals and financial capabilities. Whether your current fixed rate is ending, you want to release equity, or you're looking to consolidate debts, remortgaging could save you thousands.",
            "At Rainstone Money, we monitor the market constantly to identify opportunities for our clients. Our brokers will review your current deal, compare it against the whole market, and recommend the best course of action for your circumstances.",
            "We handle the entire remortgage process from start to finish, liaising with your current lender, solicitors, and the new lender to ensure a smooth and stress-free transition."
        ],
        [
            scard("exchange-alt", "Rate Switch", "Move to a better deal", "Your fixed rate ending? Don't default to your lender's SVR. We'll find you a competitive new deal that could save you hundreds per month."),
            scard("coins", "Equity Release", "Unlock your home's value", "Release equity from your property for home improvements, investments, or other purposes. We'll find the most cost-effective way to access your funds."),
            scard("compress-alt", "Debt Consolidation", "Simplify your finances", "Consolidate higher-interest debts into your mortgage for potentially lower monthly payments. We'll advise whether this makes financial sense for you.")
        ],
        [
            vcard("calculator", "Free Review", "We'll review your current mortgage at no cost and show you exactly how much you could save by switching to a new deal."),
            vcard("bolt", "Quick Process", "Our streamlined remortgage process means less paperwork and faster completions, so you start saving sooner."),
            vcard("handshake", "No Obligation", "Our initial consultation is completely free and without obligation. We'll only recommend switching if it genuinely benefits you."),
            vcard("user-tie", "Dedicated Advisor", "You'll have a named advisor who handles your case from start to finish, keeping you informed at every step.")
        ],
        "Start Saving Today",
        "Check If You Could Save"),
    "Ready to switch? Connect with our remortgage specialists for a free review of your current deal."
)

# 3. LIFETIME MORTGAGES
make_page("lifetime-mortgages.html", "Lifetime Mortgages",
    "Lifetime mortgage and equity release specialists at Rainstone Money. Access the wealth in your home while continuing to live there. Expert later-life lending advice.",
    hero_html("Later-Life Lending Specialists",
        'Lifetime <em class="text-gold-italic">Mortgages</em>',
        "Unlock Your Home's Value",
        'Equity release specialists <span class="gold-dot">&middot;</span> No monthly repayments required <span class="gold-dot">&middot;</span> Stay in your home'),
    solutions_html("LIFETIME MORTGAGES", "Equity Release &amp;", "Later-Life Lending",
        "Expert Lifetime Mortgage Advice",
        [
            "A lifetime mortgage is a type of equity release that lets you access the wealth tied up in your home without having to sell it or move out. You retain full ownership and can continue living in your property for as long as you wish.",
            "At Rainstone Money, our specialist later-life lending advisors understand the unique needs of homeowners aged 55 and over. We'll explain all the options available, including lump sum and drawdown lifetime mortgages, and help you understand the long-term implications.",
            "We only work with lenders who are members of the Equity Release Council, ensuring you benefit from important safeguards including the no-negative-equity guarantee."
        ],
        [
            scard("home", "Lump Sum Release", "Access your equity", "Receive a tax-free lump sum from your property's value. Use it for anything from home improvements to helping family members onto the property ladder."),
            scard("faucet-drip", "Drawdown Lifetime", "Flexible access", "Take an initial amount then draw down further funds as and when you need them. You only pay interest on what you've drawn, keeping costs lower."),
            scard("heart", "Inheritance Protection", "Protect your legacy", "Ring-fence a percentage of your property's value to guarantee an inheritance for your loved ones, giving you peace of mind.")
        ],
        [
            vcard("shield-halved", "Council Members Only", "We only recommend products from Equity Release Council members, providing you with important consumer protections."),
            vcard("users", "Family Involvement", "We encourage you to involve family in the process so everyone understands the decision and its implications."),
            vcard("scale-balanced", "Impartial Advice", "Our advisors provide balanced, impartial guidance on whether equity release is right for you and which product suits best."),
            vcard("phone-alt", "Lifetime Support", "Our relationship continues after completion. We're here to answer questions and review your plan whenever you need.")
        ],
        "Explore Equity Release Options",
        "Get a Free Assessment"),
    "Considering equity release? Speak to our later-life lending specialists for impartial advice."
)

# 4. OFFSET MORTGAGES
make_page("offset-mortgages.html", "Offset Mortgages",
    "Offset mortgage specialists at Rainstone Money. Use your savings to reduce mortgage interest and pay off your home faster with expert advice.",
    hero_html("Smart Savings Strategy",
        'Offset <em class="text-gold-italic">Mortgages</em>',
        "Make Your Savings Work Harder",
        'Reduce interest payments <span class="gold-dot">&middot;</span> Keep access to savings <span class="gold-dot">&middot;</span> Pay off faster'),
    solutions_html("OFFSET MORTGAGES", "Use Your Savings to Reduce", "Interest",
        "How Offset Mortgages Work",
        [
            "An offset mortgage links your savings and current accounts to your mortgage balance. Instead of earning interest on your savings, that amount is offset against your mortgage, so you only pay interest on the difference.",
            "For example, if you have a &pound;200,000 mortgage and &pound;30,000 in savings, you'd only pay interest on &pound;170,000. Your savings remain accessible, but by offsetting them you could save thousands in interest or pay off your mortgage years earlier.",
            "Rainstone Money works with specialist lenders who offer competitive offset mortgage products, helping you find the arrangement that maximises the benefit of your savings."
        ],
        [
            scard("piggy-bank", "Full Offset", "100% savings offset", "Your entire savings balance is offset against your mortgage. The more you save, the less interest you pay, potentially saving thousands over the mortgage term."),
            scard("family", "Family Offset", "Link family savings", "Some offset mortgages allow family members to link their savings too, helping first-time buyers benefit from their family's combined savings."),
            scard("unlock", "Flexible Access", "Keep your savings accessible", "Unlike overpayments, your savings remain yours to access whenever needed. You get the interest-saving benefit without locking your money away.")
        ],
        [
            vcard("calculator", "Interest Savings", "See exactly how much you could save by offsetting your savings against your mortgage balance with our expert calculations."),
            vcard("clock", "Pay Off Faster", "By reducing your interest, more of each payment goes towards your mortgage balance, helping you become mortgage-free sooner."),
            vcard("shield-halved", "Tax Efficient", "Offset mortgages can be particularly tax-efficient for higher and additional rate taxpayers who would pay 40-45% on savings interest."),
            vcard("handshake", "Expert Matching", "We'll assess whether an offset mortgage is right for you and find the most competitive product from our specialist lender panel.")
        ],
        "Explore Offset Options",
        "See How Much You Could Save"),
    "Interested in offsetting your savings? Speak to our mortgage experts for a personalised assessment."
)

# 5. DEVELOPMENT FINANCE
make_page("development-finance.html", "Development Finance",
    "Development finance specialists at Rainstone Money. Funding for ground-up builds, conversions, and refurbishments. Expert guidance from experienced brokers.",
    hero_html("Property Development Specialists",
        'Development <em class="text-gold-italic">Finance</em>',
        "Fund Your Next Project",
        'Ground-up builds <span class="gold-dot">&middot;</span> Conversions &amp; refurbishments <span class="gold-dot">&middot;</span> Experienced developers'),
    solutions_html("DEVELOPMENT FINANCE", "Funding Your Property", "Development",
        "Expert Development Finance Solutions",
        [
            "Development finance provides the funding needed to purchase land and cover construction costs for residential and commercial property developments. Whether you're planning a ground-up new build, a conversion project, or a major refurbishment, we arrange the right funding structure.",
            "At Rainstone Money, we work with specialist development finance lenders who understand the complexities of property development. We've successfully arranged funding for projects ranging from single-unit conversions to large multi-unit developments worth over &pound;14 million.",
            "Our team has deep experience in structuring development finance deals, including staged drawdowns, mezzanine finance, and joint venture arrangements to maximise your project's potential."
        ],
        [
            scard("building", "Ground-Up Development", "New build funding", "Complete funding solutions for new build developments, from land acquisition through to construction completion. Staged drawdowns aligned to your build programme."),
            scard("hammer", "Refurbishment Finance", "Light to heavy refurb", "Whether it's a light cosmetic refurbishment or a heavy structural renovation, we arrange finance tailored to the scope and timeline of your project."),
            scard("warehouse", "Commercial Development", "Industrial &amp; mixed use", "Funding for commercial developments including industrial units, warehouses, retail spaces, and mixed-use schemes with complex planning requirements.")
        ],
        [
            vcard("chart-line", "Competitive Rates", "Access development finance from 5.5% with competitive arrangement fees. We negotiate the best terms based on your experience and project viability."),
            vcard("list-check", "Staged Drawdowns", "Funds released in stages as your build progresses, monitored by an independent surveyor to protect both you and the lender."),
            vcard("handshake", "Lender Relationships", "Our established relationships with development lenders mean faster decisions and access to funding that isn't available on the open market."),
            vcard("user-tie", "Project Support", "Beyond funding, we can connect you with solicitors, surveyors, and other professionals experienced in development projects.")
        ],
        "Discuss Your Development",
        "Get Development Finance"),
    "Planning a development? Speak to our development finance team for expert funding advice.",
    mode="commercial"
)

# 6. COMMERCIAL FINANCE
make_page("commercial-finance.html", "Commercial Finance",
    "Commercial finance brokers at Rainstone Money. Expert funding solutions for businesses including commercial mortgages, asset finance, and working capital.",
    hero_html("Commercial Finance Specialists",
        'Commercial <em class="text-gold-italic">Finance</em>',
        "Solutions for Business",
        'Tailored business funding <span class="gold-dot">&middot;</span> Specialist lender access <span class="gold-dot">&middot;</span> Expert guidance',
        "tab-commercial"),
    solutions_html("COMMERCIAL FINANCE", "Funding Solutions for", "Your Business",
        "Expert Commercial Finance Advice",
        [
            "Rainstone Money is a trusted commercial finance broker providing flexible funding solutions for businesses of all sizes. Commercial mortgage rates play a crucial role in determining the cost of borrowing, and our expertise ensures you get the most competitive terms available.",
            "Our Commercial Finance division works with business owners, property developers, and investors to arrange funding solutions tailored to their needs. From commercial mortgages to asset finance and working capital facilities, we provide strategies designed to support growth and long-term success.",
            "With access to specialist commercial lenders, challenger banks, and private funding sources, we can arrange finance for complex situations that high-street banks may decline."
        ],
        [
            scard("landmark", "Commercial Mortgages", "Property acquisition", "Finance for purchasing or refinancing commercial property including offices, retail units, industrial premises, and mixed-use buildings."),
            scard("coins", "Asset Finance", "Equipment &amp; vehicles", "Fund essential business equipment, vehicles, and machinery without tying up working capital. Flexible terms from 1 to 7 years."),
            scard("chart-pie", "Working Capital", "Cash flow solutions", "Invoice finance, overdraft facilities, and revolving credit to keep your business running smoothly and fund growth opportunities.")
        ],
        [
            vcard("handshake", "Trusted Partnerships", "We've built strong relationships with commercial lenders, giving you access to exclusive products and faster decision-making."),
            vcard("users", "Sector Expertise", "Our team has experience across all commercial sectors including retail, hospitality, healthcare, manufacturing, and professional services."),
            vcard("shield-halved", "Structured Solutions", "Complex funding needs require structured solutions. We design bespoke arrangements that align with your business objectives."),
            vcard("chart-line", "Growth Focused", "We don't just arrange finance — we help you choose the right funding structure to support your business growth strategy.")
        ],
        "Explore Commercial Solutions",
        "Speak to a Commercial Expert",
        "tab-commercial"),
    "Ready to fund your business growth? Connect with our commercial finance team for expert advice.",
    mode="commercial"
)

# 7. COMMERCIAL MORTGAGES
make_page("commercial-mortgages.html", "Commercial Mortgages",
    "Commercial mortgage specialists at Rainstone Money. Competitive rates for purchasing or refinancing commercial property. Award-winning broker expertise.",
    hero_html("Commercial Property Experts",
        'Commercial <em class="text-gold-italic">Mortgages</em>',
        "Property Finance Made Simple",
        'Competitive rates <span class="gold-dot">&middot;</span> All property types <span class="gold-dot">&middot;</span> Fast decisions',
        "tab-commercial"),
    solutions_html("COMMERCIAL MORTGAGES", "Finance for Commercial", "Property",
        "Specialist Commercial Mortgage Advice",
        [
            "A commercial mortgage is a loan secured against a commercial property, whether you're purchasing, refinancing, or releasing equity from business premises. Terms typically range from 3 to 25 years with both fixed and variable rate options available.",
            "Rainstone Money arranges commercial mortgages for all property types including offices, retail units, warehouses, industrial premises, pubs, restaurants, care homes, and mixed-use buildings. We understand the nuances of each sector and match you with the right lender.",
            "Whether you're an owner-occupier buying your business premises or an investor building a commercial property portfolio, our expertise ensures you get the most competitive terms and a smooth application process."
        ],
        [
            scard("building", "Owner-Occupier", "Buy your premises", "Purchase the premises your business operates from. Stop paying rent and build equity in your own commercial property with competitive mortgage terms."),
            scard("chart-line", "Investment Property", "Portfolio building", "Finance for purchasing commercial investment properties. We work with lenders experienced in multi-let, single-let, and mixed commercial portfolios."),
            scard("exchange-alt", "Refinancing", "Better terms", "Refinance your existing commercial mortgage to access better rates, release equity, or restructure your borrowing for improved cash flow.")
        ],
        [
            vcard("percent", "Competitive Rates", "Access rates from leading commercial lenders, challenger banks, and specialist funders through our extensive lender panel."),
            vcard("bolt", "Fast Decisions", "Our lender relationships mean faster credit decisions. Many applications receive an indicative terms within 48 hours."),
            vcard("file-alt", "Less Paperwork", "We prepare your application to lender standards first time, reducing delays and the need for additional information requests."),
            vcard("user-tie", "Named Contact", "A dedicated broker manages your case throughout, providing a single point of contact from enquiry to completion.")
        ],
        "Get a Commercial Mortgage Quote",
        "Get Your Quote",
        "tab-commercial"),
    "Looking for a commercial mortgage? Contact our specialists for competitive rates and expert advice.",
    mode="commercial"
)

# 8. BRIDGING LOANS
make_page("bridging-loan.html", "Bridging Loans",
    "Bridging loan specialists at Rainstone Money. Fast, flexible short-term finance for property purchases, auction buys, and chain breaks. Decisions in 24 hours.",
    hero_html("Fast, Flexible Finance",
        'Bridging <em class="text-gold-italic">Loans</em>',
        "When Speed Matters",
        'Funds in days <span class="gold-dot">&middot;</span> Auction finance <span class="gold-dot">&middot;</span> Chain break solutions',
        "tab-commercial"),
    solutions_html("BRIDGING LOANS", "Short-Term Finance,", "Fast Decisions",
        "Expert Bridging Finance Solutions",
        [
            "Bridging loans offer a means to secure a substantial sum for a brief duration. They're primarily used to 'bridge the gap' in property transactions, such as facilitating the purchase of a new property before the sale of an existing one is finalised.",
            "At Rainstone Money, we arrange bridging loans from &pound;50,000 to &pound;25 million with terms from 1 to 24 months. Our established lender relationships mean we can often secure funding within days, making us the ideal partner for time-sensitive property transactions.",
            "Whether you need auction finance within 28 days, a chain break solution, or short-term funding for a refurbishment project, our experienced team will structure the right bridging solution for your needs."
        ],
        [
            scard("gavel", "Auction Finance", "28-day completion", "Secured a property at auction? We arrange bridging finance to meet the strict 28-day completion deadline, with funds available within days of your successful bid."),
            scard("link-slash", "Chain Break", "Don't lose your purchase", "Found your next property but haven't sold your current one? A bridging loan lets you complete the purchase while your sale goes through, preventing chain collapse."),
            scard("hammer", "Refurbishment", "Uninhabitable properties", "Finance for properties that don't qualify for a traditional mortgage due to their condition. Bridge the gap while you renovate, then refinance onto a long-term mortgage.")
        ],
        [
            vcard("bolt", "Speed", "Bridging loans can complete in as little as 7 days. Our streamlined process and lender relationships ensure the fastest possible turnaround."),
            vcard("sliders", "Flexibility", "Interest can be rolled up, serviced monthly, or deducted upfront. We structure repayments to suit your cash flow and exit strategy."),
            vcard("door-open", "Clear Exit Strategy", "We ensure every bridging loan has a viable exit strategy, whether that's a sale, refinance, or development completion."),
            vcard("handshake", "Expert Structuring", "Complex bridging cases are our speciality. We arrange first and second charge bridges, including for non-standard properties and situations.")
        ],
        "Discuss Your Bridging Needs",
        "Get Bridging Finance",
        "tab-commercial"),
    "Need fast finance? Speak to our bridging loan specialists for a rapid assessment.",
    mode="commercial"
)

# 9. BUSINESS LOANS
make_page("business-loans.html", "Business Loans",
    "Business loan brokers at Rainstone Money. Flexible funding solutions including term loans, lines of credit, and equipment financing for UK businesses.",
    hero_html("Business Funding Specialists",
        'Business <em class="text-gold-italic">Loans</em>',
        "Fuel Your Growth",
        'Term loans <span class="gold-dot">&middot;</span> Lines of credit <span class="gold-dot">&middot;</span> Equipment financing',
        "tab-commercial"),
    solutions_html("BUSINESS LOANS", "Flexible Funding for", "Business Growth",
        "Tailored Business Finance Solutions",
        [
            "Whether it's a term loan, line of credit, equipment financing, or factoring &mdash; our commercial finance options are structured to provide resilience, offering adaptable terms and support mechanisms to help your business navigate changing economic landscapes.",
            "Rainstone Money works with a wide panel of business lenders including high-street banks, challenger banks, alternative lenders, and private funding sources. This breadth of access means we can find solutions for businesses at every stage, from start-ups to established enterprises.",
            "Our business finance team takes the time to understand your objectives, cash flow patterns, and growth plans before recommending a funding solution. This consultative approach ensures the finance we arrange truly supports your business strategy."
        ],
        [
            scard("money-bill-wave", "Term Loans", "Structured borrowing", "Fixed or variable rate business loans with terms from 1 to 25 years. Ideal for expansion, acquisitions, or large capital expenditure with predictable repayments."),
            scard("rotate", "Revolving Credit", "Flexible access", "Draw down and repay as needed with a revolving credit facility. Only pay interest on what you use, giving your business maximum flexibility."),
            scard("truck", "Asset Finance", "Fund equipment", "Spread the cost of essential equipment, vehicles, and machinery. Preserve your working capital while investing in the tools your business needs to grow.")
        ],
        [
            vcard("chart-line", "Growth Focused", "We understand that business finance is about enabling growth. Our solutions are designed to support your strategic objectives."),
            vcard("users", "All Sectors", "We arrange business finance across all industries including construction, hospitality, healthcare, retail, manufacturing, and professional services."),
            vcard("clock", "Fast Decisions", "Many of our lending partners can provide indicative terms within 24 hours, with funding available in as little as 5 working days."),
            vcard("handshake", "Ongoing Relationship", "We review your business funding needs regularly, ensuring your finance arrangements continue to match your evolving requirements.")
        ],
        "Explore Business Finance Options",
        "Get Business Funding",
        "tab-commercial"),
    "Looking for business funding? Contact our commercial team for tailored solutions.",
    mode="commercial"
)

# 10. FOREIGN NATIONALS
make_page("foreign-nationals.html", "Foreign National Mortgages",
    "Mortgage specialists for foreign nationals at Rainstone Money. Expert advice for non-UK residents and expats looking to purchase UK property.",
    hero_html("UK Property for International Buyers",
        'Foreign National <em class="text-gold-italic">Mortgages</em>',
        "Invest in UK Property",
        'Non-UK residents <span class="gold-dot">&middot;</span> Expat specialists <span class="gold-dot">&middot;</span> Overseas income accepted'),
    solutions_html("FOREIGN NATIONALS", "UK Mortgages for", "International Buyers",
        "Specialist Foreign National Advice",
        [
            "Purchasing property in the UK as a foreign national or expat can be challenging. Many high-street lenders have restrictive criteria that exclude non-UK residents, but specialist lenders actively welcome international buyers.",
            "Rainstone Money has extensive experience in arranging mortgages for foreign nationals, expats, and non-UK residents. We've successfully helped clients from across the globe purchase UK residential and investment property, even when they've been rejected by other brokers.",
            "Whether you're a foreign national living overseas, a UK expat working abroad, or an international investor, our specialist team understands the unique requirements of overseas income, different currencies, and varying tax situations."
        ],
        [
            scard("globe", "Overseas Residents", "Non-UK based buyers", "Mortgages for foreign nationals living outside the UK. We work with lenders who accept overseas income, foreign currencies, and international credit histories."),
            scard("plane", "UK Expats", "Working abroad", "UK nationals living and working overseas can find it difficult to get a UK mortgage. Our specialist lenders understand expat income and employment structures."),
            scard("building", "Investment Purchases", "BTL for international buyers", "Buy-to-let mortgages for foreign national investors. Build a UK property portfolio with specialist lending tailored to international investors.")
        ],
        [
            vcard("language", "Multi-Currency", "We work with lenders who accept income in all major currencies and understand international banking and tax arrangements."),
            vcard("passport", "Visa Expertise", "Our team understands how different visa types and residency status affect mortgage eligibility and can advise accordingly."),
            vcard("handshake", "Proven Track Record", "We've successfully arranged hundreds of mortgages for foreign nationals, including cases rejected by multiple other brokers."),
            vcard("user-tie", "Dedicated Support", "Your dedicated advisor will guide you through every step, managing time zones and communication to make the process seamless.")
        ],
        "Start Your UK Property Journey",
        "Get Expert Advice"),
    "International buyer? Connect with our foreign national mortgage specialists for expert guidance."
)

# 11. BUILDING INSURANCE
make_page("building-insurance.html", "Building Insurance",
    "Building insurance from Rainstone Money. Protect your property with comprehensive buildings cover tailored to homeowners and landlords.",
    hero_html("Protect Your Property",
        'Building <em class="text-gold-italic">Insurance</em>',
        "Comprehensive Cover",
        'Homeowner protection <span class="gold-dot">&middot;</span> Landlord cover <span class="gold-dot">&middot;</span> Competitive premiums'),
    solutions_html("BUILDING INSURANCE", "Protecting Your Property", "Investment",
        "Expert Building Insurance Advice",
        [
            "Building insurance covers the cost of repairing or rebuilding your property if it's damaged by events like fire, flooding, storms, or subsidence. Most mortgage lenders require you to have building insurance in place as a condition of your mortgage.",
            "At Rainstone Money, we help you find the right level of buildings cover at a competitive premium. We compare policies from leading insurers to ensure your property is fully protected without paying more than you need to.",
            "Whether you're a homeowner, landlord, or property investor, we'll find a buildings insurance policy that covers the full rebuild cost of your property and includes the protections that matter most to you."
        ],
        [
            scard("home", "Homeowner Cover", "Protect your home", "Comprehensive buildings insurance for homeowners covering structural damage, fixtures and fittings, and permanent structures within your property boundary."),
            scard("building", "Landlord Cover", "Protect your investment", "Specialist building insurance for rental properties with additional covers for landlord-specific risks including malicious damage by tenants."),
            scard("layer-group", "Portfolio Cover", "Multiple properties", "Multi-property building insurance for portfolio landlords with competitive rates that decrease as you add more properties to your policy.")
        ],
        [
            vcard("shield-halved", "Full Protection", "Every policy we arrange covers the full rebuild cost of your property, ensuring you're never underinsured."),
            vcard("percent", "Competitive Rates", "We compare premiums from leading insurers to find you comprehensive cover at the best possible price."),
            vcard("file-alt", "Simple Claims", "We work with insurers known for straightforward claims processes, so you're supported when you need it most."),
            vcard("phone-alt", "Ongoing Support", "Need to update your cover or make a claim? We're here to help throughout the life of your policy.")
        ],
        "Get a Building Insurance Quote",
        "Get Your Quote"),
    "Need building insurance? Contact our team for competitive quotes and expert advice."
)

# 12. CONTENT INSURANCE
make_page("content-insurance.html", "Contents Insurance",
    "Contents insurance from Rainstone Money. Protect your belongings with comprehensive cover for homeowners, tenants, and landlords.",
    hero_html("Protect What's Inside",
        'Contents <em class="text-gold-italic">Insurance</em>',
        "Cover Your Belongings",
        'Personal possessions <span class="gold-dot">&middot;</span> Accidental damage <span class="gold-dot">&middot;</span> Valuables cover'),
    solutions_html("CONTENTS INSURANCE", "Protecting Your", "Belongings",
        "Expert Contents Insurance Advice",
        [
            "Contents insurance protects your personal belongings against theft, loss, and damage. From furniture and electronics to jewellery and clothing, a good contents policy ensures you can replace your possessions if the worst happens.",
            "Rainstone Money compares contents insurance from leading providers to find the right level of cover for your needs. We'll help you calculate the true replacement value of your contents and ensure nothing important is left unprotected.",
            "Whether you need standard contents cover, high-value item protection, or specialist landlord contents insurance, our advisors will find the best policy at a competitive price."
        ],
        [
            scard("couch", "Home Contents", "Protect your possessions", "Comprehensive cover for all your household contents including furniture, electronics, appliances, and personal items against theft, fire, and flood."),
            scard("gem", "Valuables Cover", "High-value items", "Extended cover for high-value items including jewellery, watches, art, and collectibles both inside and outside your home."),
            scard("laptop", "Away from Home", "Portable items", "Protect your belongings when you're away from home, including laptops, phones, and other portable electronics against loss and accidental damage.")
        ],
        [
            vcard("calculator", "Accurate Valuation", "We help you calculate the true replacement value of your contents so you're never underinsured when you need to claim."),
            vcard("shield-halved", "Comprehensive Cover", "Protection against theft, fire, flood, storm damage, and accidental damage with options to tailor cover to your exact needs."),
            vcard("percent", "Best Prices", "We compare policies from multiple insurers to find comprehensive cover at the most competitive premium."),
            vcard("phone-alt", "Claims Support", "If you need to make a claim, we're on hand to guide you through the process and liaise with your insurer on your behalf.")
        ],
        "Get a Contents Insurance Quote",
        "Get Your Quote"),
    "Need contents cover? Contact our insurance team for a competitive, tailored quote."
)

# 13. LANDLORD INSURANCE
make_page("landlord-insurance.html", "Landlord Insurance",
    "Specialist landlord insurance from Rainstone Money. Comprehensive cover for rental properties including buildings, contents, liability, and rent guarantee.",
    hero_html("Protection for Landlords",
        'Landlord <em class="text-gold-italic">Insurance</em>',
        "Protect Your Rental Income",
        'Property cover <span class="gold-dot">&middot;</span> Rent guarantee <span class="gold-dot">&middot;</span> Liability protection'),
    solutions_html("LANDLORD INSURANCE", "Comprehensive Cover for", "Rental Properties",
        "Specialist Landlord Insurance",
        [
            "As a landlord, you face unique risks that standard home insurance doesn't cover. Landlord insurance is specifically designed to protect your rental property, rental income, and your legal liability as a property owner.",
            "Rainstone Money works with specialist landlord insurers to arrange comprehensive cover packages that protect every aspect of your rental business. From single property landlords to portfolio investors, we find the right level of protection.",
            "Our landlord insurance packages can include buildings cover, landlord contents, rent guarantee, legal expenses, and public liability &mdash; all tailored to your specific portfolio and tenancy arrangements."
        ],
        [
            scard("home", "Property Protection", "Buildings &amp; contents", "Comprehensive cover for the structure of your rental property and any contents you provide, including protection against malicious damage by tenants."),
            scard("money-bill-wave", "Rent Guarantee", "Protect your income", "Rent guarantee insurance covers your rental income if tenants default on payments, ensuring your cash flow remains stable even during void periods."),
            scard("gavel", "Legal Protection", "Expenses covered", "Legal expenses cover for disputes with tenants, including eviction proceedings, rent recovery, and property damage claims.")
        ],
        [
            vcard("layer-group", "Portfolio Discounts", "Multi-property landlords benefit from portfolio discounts, reducing your per-property premium as your portfolio grows."),
            vcard("shield-halved", "Full Coverage", "Every policy covers the specific risks landlords face, from tenant damage to liability claims and loss of rent."),
            vcard("bolt", "Quick Quotes", "Get a competitive landlord insurance quote within minutes, with cover available from the same day."),
            vcard("handshake", "Claims Assistance", "When you need to claim, our team supports you through the process to ensure a fair and timely settlement.")
        ],
        "Get Landlord Insurance",
        "Get Your Quote"),
    "Landlord? Protect your rental properties with our specialist insurance. Get a quote today."
)

# 14. RENTERS INSURANCE
make_page("renters-insurance.html", "Renters Insurance",
    "Renters insurance from Rainstone Money. Protect your belongings as a tenant with affordable contents cover and personal liability protection.",
    hero_html("Protection for Tenants",
        'Renters <em class="text-gold-italic">Insurance</em>',
        "Cover Your Belongings",
        'Tenant contents cover <span class="gold-dot">&middot;</span> Personal liability <span class="gold-dot">&middot;</span> Affordable premiums'),
    solutions_html("RENTERS INSURANCE", "Insurance for", "Tenants",
        "Affordable Renters Insurance",
        [
            "As a tenant, your landlord's insurance covers the building but not your personal belongings. Renters insurance protects your possessions against theft, fire, flood, and accidental damage, giving you peace of mind in your rented home.",
            "Rainstone Money helps tenants find affordable contents insurance that covers everything from furniture and electronics to clothing and personal items. We'll ensure you have the right level of cover without overpaying.",
            "Our renters insurance policies can also include personal liability cover, protecting you if you accidentally damage the property or someone is injured in your home."
        ],
        [
            scard("couch", "Contents Cover", "Protect your belongings", "Cover all your personal possessions in your rented home against theft, fire, flood, and storm damage at an affordable monthly premium."),
            scard("exclamation-triangle", "Accidental Damage", "Everyday accidents", "Accidental damage cover protects against everyday mishaps like spilt drinks on laptops or dropped phones, keeping you covered for the unexpected."),
            scard("user-shield", "Personal Liability", "Protect yourself", "If you accidentally damage your rental property or a visitor is injured, personal liability cover protects you against claims and legal costs.")
        ],
        [
            vcard("percent", "Affordable Premiums", "Renters insurance is surprisingly affordable, often costing less than a takeaway coffee per week for comprehensive cover."),
            vcard("bolt", "Instant Cover", "Get covered immediately with policies that start from the day you apply, so your belongings are protected from day one."),
            vcard("laptop", "Away from Home", "Many renters policies include cover for belongings taken outside the home, protecting your phone, laptop, and other portable items."),
            vcard("phone-alt", "Easy Claims", "Simple, straightforward claims process so you can get your belongings replaced quickly if the worst happens.")
        ],
        "Get Renters Insurance",
        "Get Your Quote"),
    "Renting? Protect your belongings with affordable renters insurance. Get a quote today."
)

# 15. FINANCIAL HEALTH CHECK
make_page("financial-health-check.html", "Financial Health Check",
    "Free financial health check from Rainstone Money. Comprehensive review of your mortgage, insurance, and financial arrangements to ensure you're getting the best deals.",
    hero_html("Review Your Finances",
        'Financial Health <em class="text-gold-italic">Check</em>',
        "Are You Getting the Best Deal?",
        'Mortgage review <span class="gold-dot">&middot;</span> Insurance audit <span class="gold-dot">&middot;</span> Savings assessment'),
    solutions_html("FINANCIAL HEALTH CHECK", "A Complete Review of", "Your Finances",
        "Your Free Financial Health Check",
        [
            "A financial health check is a comprehensive review of your entire financial position. We examine your mortgage, insurance policies, savings, investments, and protection arrangements to identify opportunities to save money and improve your financial wellbeing.",
            "Many people are paying more than they need to on their mortgage, have gaps in their insurance cover, or are missing out on better savings rates. Our free financial health check identifies these opportunities and provides clear, actionable recommendations.",
            "At Rainstone Money, we believe everyone deserves to know where they stand financially. That's why our health check is completely free and comes with no obligation to act on our recommendations."
        ],
        [
            scard("stethoscope", "Mortgage Review", "Check your rate", "We'll compare your current mortgage against the whole market to see if you could save money by switching to a better deal."),
            scard("shield-halved", "Insurance Audit", "Check your cover", "We'll review all your insurance policies to ensure you have adequate cover and aren't paying over the odds for protection you don't need."),
            scard("piggy-bank", "Savings Review", "Optimise your money", "We'll look at your savings and investments to ensure your money is working as hard as possible and identify any tax-efficient opportunities.")
        ],
        [
            vcard("gift", "Completely Free", "Our financial health check costs nothing and comes with absolutely no obligation to take any action on our recommendations."),
            vcard("clock", "30-Minute Review", "Your health check takes just 30 minutes and can be done over the phone or in person at one of our offices."),
            vcard("file-alt", "Written Report", "You'll receive a clear written summary of our findings and recommendations that you can review in your own time."),
            vcard("calendar", "Annual Reviews", "We offer annual reviews to ensure your financial arrangements continue to meet your needs as circumstances change.")
        ],
        "Book Your Free Health Check",
        "Book Your Review"),
    "Want to know if you're getting the best deal? Book your free financial health check today."
)

# 16. FINANCIAL PLANNING
make_page("financial-planning.html", "Financial Planning",
    "Expert financial planning from Rainstone Money. Protection, pensions, investments, and wealth management advice tailored to your goals and circumstances.",
    hero_html("Plan Your Financial Future",
        'Financial <em class="text-gold-italic">Planning</em>',
        "Secure Your Future",
        'Protection planning <span class="gold-dot">&middot;</span> Wealth management <span class="gold-dot">&middot;</span> Retirement planning'),
    solutions_html("FINANCIAL PLANNING", "Expert Advice for Your", "Financial Future",
        "Comprehensive Financial Planning",
        [
            "Financial planning is about more than just money &mdash; it's about achieving your life goals. Whether you're planning for retirement, protecting your family, or building wealth, our advisors create a personalised strategy that puts you on the right path.",
            "At Rainstone Money, our financial planning team takes a holistic approach, considering your complete financial picture including income, expenditure, assets, liabilities, and future objectives. This ensures every recommendation is aligned with your broader goals.",
            "We provide ongoing reviews and support to ensure your financial plan evolves with you, adapting to life changes and market conditions to keep you on track."
        ],
        [
            scard("umbrella", "Protection Planning", "Secure your family", "Life insurance, critical illness cover, and income protection designed to safeguard your family's financial security if the unexpected happens."),
            scard("chart-line", "Investment Advice", "Grow your wealth", "Expert investment guidance to help you build wealth over time, with strategies tailored to your risk appetite and time horizons."),
            scard("user-clock", "Retirement Planning", "Plan for the future", "Pension reviews, retirement income planning, and strategies to ensure you can enjoy the retirement lifestyle you deserve.")
        ],
        [
            vcard("compass", "Holistic Approach", "We consider your entire financial picture, not just individual products, ensuring every recommendation supports your overall goals."),
            vcard("handshake", "Fee Transparency", "Our fee structure is completely transparent and agreed upfront, so you always know exactly what you're paying for."),
            vcard("rotate", "Regular Reviews", "Circumstances change, and so should your financial plan. We conduct regular reviews to keep your strategy on track."),
            vcard("user-tie", "Qualified Advisors", "Our financial planners hold the highest industry qualifications and are committed to acting in your best interests at all times.")
        ],
        "Book a Financial Planning Session",
        "Start Planning Today"),
    "Ready to plan your financial future? Book a session with our expert financial planners."
)

# 17. WHO WE ARE
make_page("who-we-are.html", "Who We Are",
    "Learn about Rainstone Money, award-winning UK finance brokers with over 100 years of combined banking experience. Founded in 2015, trusted by thousands.",
    hero_html("Award-Winning Finance Brokers",
        'About <em class="text-gold-italic">Rainstone Money</em>',
        "Our Story",
        'Founded 2015 <span class="gold-dot">&middot;</span> 100+ years combined experience <span class="gold-dot">&middot;</span> Award-winning team'),
    solutions_html("ABOUT US", "Built by Bankers, Driven by", "Relationships",
        "Our Story",
        [
            "Founded in 2015, Rainstone Money has been built by ex-professional bankers with a combined experience of over 100 years within the commercial finance and property industry. We have taken great pride in building long-lasting relationships with our clients and supporting them with all of their financial needs.",
            "We are experts in commercial finance, mortgages, development funding, bridging finance, business loans, asset finance, invoice finance, and insurance. Our team brings deep institutional knowledge from careers at major UK banks, combined with the agility and personal service that only an independent brokerage can offer.",
            "Rainstone Money Commercial Finance was launched as a distinct arm of Rainstone Money Group to deliver a more focused and specialist service for complex commercial finance needs and high-net-worth individuals. This enables us to provide tailored, innovative solutions with a premium, hands-on approach."
        ],
        [
            scard("trophy", "Multi Award-Winning", "Industry recognised", "BTL Broker of the Year 2024, Best Brokerage Firm, Excellence in Financial Services, and Most Innovative Commercial Finance Specialists."),
            scard("users", "Expert Team", "Banking professionals", "Our team comprises former senior bankers, qualified mortgage advisors, and specialist commercial finance brokers with decades of experience."),
            scard("heart", "Client First", "Relationship driven", "We believe in building long-term relationships, not transactional ones. Many of our clients have been with us since we launched in 2015.")
        ],
        [
            vcard("handshake", "Integrity", "We believe in doing the right thing, acting transparently in every interaction. Our commitment to honesty ensures you get advice that truly serves your interests."),
            vcard("users", "Client Focus", "Your goals are our priority. We take the time to understand your unique situation and tailor our approach to deliver solutions that work for you."),
            vcard("shield-halved", "Risk Resilience", "Finance involves risk, and we ensure you understand every decision. Our experienced team builds solutions that protect your interests."),
            vcard("chart-line", "Expertise", "With over 100 years of combined experience, our team brings deep industry knowledge to every case, ensuring access to the best products available.")
        ],
        "Get in Touch",
        "Contact Us"),
    "Want to learn more about Rainstone Money? We'd love to hear from you."
)

# 18. MEET THE TEAM
make_page("meet-the-team.html", "Meet The Team",
    "Meet the team at Rainstone Money. Our expert brokers and advisors bring over 100 years of combined banking experience to help you achieve your financial goals.",
    hero_html("The People Behind Rainstone",
        'Meet The <em class="text-gold-italic">Team</em>',
        "Expert Advisors",
        'Qualified professionals <span class="gold-dot">&middot;</span> Banking experience <span class="gold-dot">&middot;</span> Dedicated to your success'),
    solutions_html("OUR TEAM", "The Experts Behind", "Rainstone Money",
        "A Team of Industry Professionals",
        [
            "At Rainstone Money, our strength lies in our people. Our team of qualified mortgage advisors, commercial finance brokers, and insurance specialists bring a wealth of experience from careers in banking and financial services.",
            "Every member of our team is committed to delivering exceptional service and outcomes for our clients. We invest heavily in ongoing professional development to ensure our knowledge remains at the cutting edge of the industry.",
            "When you work with Rainstone Money, you're assigned a dedicated advisor who manages your case from start to finish. They'll be your single point of contact, keeping you informed at every stage."
        ],
        [
            scard("user-tie", "Foyaz Ahmed", "CEO &amp; Founder", "With extensive experience in banking and financial services, Foyaz founded Rainstone Money in 2015 with a vision to deliver truly independent, client-focused financial advice."),
            scard("user-tie", "Rahul Modasia", "Director of Commercial", "Rahul leads our Commercial, Bridging, and Development Finance division, bringing deep expertise in structuring complex funding solutions for businesses and developers."),
            scard("user-tie", "Expert Advisors", "Our wider team", "Our team of qualified advisors, analysts, and support staff work together to ensure every client receives the highest standard of service and the best possible outcome.")
        ],
        [
            vcard("graduation-cap", "Qualified", "Every advisor holds relevant professional qualifications and is registered with the appropriate regulatory bodies."),
            vcard("handshake", "Dedicated", "Each client is assigned a named advisor who takes personal responsibility for their case from enquiry to completion."),
            vcard("comments", "Accessible", "We pride ourselves on being easy to reach. Your advisor is available by phone, email, or in person at our offices."),
            vcard("award", "Recognised", "Our team has been recognised with multiple industry awards for excellence in financial services and client care.")
        ],
        "Get in Touch With Our Team",
        "Contact the Team"),
    "Want to speak with one of our expert advisors? Get in touch today."
)

# 19. NETWORK
make_page("network.html", "Join Our Network",
    "Join the Rainstone Money network. Opportunities for mortgage advisors, commercial brokers, and financial professionals. Grow your career with an award-winning firm.",
    hero_html("Grow Your Career",
        'Join Our <em class="text-gold-italic">Network</em>',
        "Become Part of Something Bigger",
        'Career opportunities <span class="gold-dot">&middot;</span> Training &amp; support <span class="gold-dot">&middot;</span> Award-winning firm'),
    solutions_html("OUR NETWORK", "Join the Rainstone Money", "Network",
        "Opportunities for Financial Professionals",
        [
            "Rainstone Money is always looking for talented mortgage advisors, commercial finance brokers, and financial professionals to join our growing network. We offer a supportive environment with access to our full lender panel, compliance support, and business development resources.",
            "Whether you're an experienced broker looking for a new home or a newly qualified advisor seeking mentorship and growth opportunities, our network provides the platform you need to succeed.",
            "As a member of the Rainstone Money network, you'll benefit from our award-winning brand, established lender relationships, marketing support, and ongoing professional development opportunities."
        ],
        [
            scard("users", "Mortgage Advisors", "Residential specialists", "Join our residential mortgage team with access to the whole market, comprehensive compliance support, and leads from our marketing channels."),
            scard("landmark", "Commercial Brokers", "Commercial specialists", "Experienced commercial finance brokers can benefit from our specialist lender relationships and back-office support to focus on what they do best."),
            scard("graduation-cap", "Trainee Advisors", "Start your career", "We offer structured training programmes for aspiring mortgage advisors, providing the qualifications, mentorship, and experience you need to build a successful career.")
        ],
        [
            vcard("building", "Full Support", "Compliance, administration, and back-office support so you can focus on advising clients and growing your business."),
            vcard("chart-line", "Growth Potential", "Competitive commission structures with clear progression pathways for ambitious professionals."),
            vcard("handshake", "Lender Access", "Full access to our extensive lender panel including specialist and exclusive products not available to individual brokers."),
            vcard("trophy", "Award-Winning Brand", "Benefit from the credibility and client confidence that comes with representing an award-winning, FCA-regulated firm.")
        ],
        "Apply to Join Our Network",
        "Apply Now"),
    "Interested in joining our network? Get in touch to discuss opportunities."
)

# 20. CASE STUDIES
make_page("case-studies.html", "Case Studies",
    "Real case studies from Rainstone Money. See how we've helped clients with complex bridging loans, buy-to-let portfolios, foreign national purchases, and development finance.",
    hero_html("Real Deals, Real Results",
        'Our Case <em class="text-gold-italic">Studies</em>',
        "Proven Track Record",
        'Complex cases solved <span class="gold-dot">&middot;</span> Millions arranged <span class="gold-dot">&middot;</span> Clients across the UK'),
    solutions_html("CASE STUDIES", "Proven Results for Our", "Clients",
        "See How We've Helped",
        [
            "At Rainstone Money, we pride ourselves on solving complex financial challenges that others can't. Our case studies demonstrate our ability to arrange substantial funding in challenging circumstances, often within tight deadlines.",
            "From saving a 7-property portfolio from repossession with a &pound;3M bridging facility completed in just 3 weeks, to arranging a &pound;7.4M development finance deal for international investors, our track record speaks for itself.",
            "Each case study highlights not just what we achieved, but how we achieved it &mdash; the creative thinking, specialist knowledge, and lender relationships that make the difference when the stakes are high."
        ],
        [
            scard("building", "&pound;5M Portfolio Rescue", "Bridging loan", "Client with seven properties facing repossession within 14 days. We arranged a &pound;3M bridging facility completing in just 3 weeks to save the entire portfolio."),
            scard("home", "Grade II Listed Manor", "BTL term loan", "High-net-worth client acquiring a historic 55-acre manor with subsidence issues. Secured the asset at &pound;1M below asking with a &pound;2.6M facility at 50% LTV."),
            scard("globe", "&pound;570K Foreign National", "Residential purchase", "Non-UK national based in the US, rejected by four brokers. No UK payslips or credit history. We structured a solution using US income and completed successfully.")
        ],
        [
            vcard("chart-line", "Complex Cases", "We specialise in cases that don't fit the standard mould, finding solutions where others see obstacles."),
            vcard("bolt", "Fast Turnaround", "Many of our most notable cases have involved tight deadlines, demonstrating our ability to work quickly under pressure."),
            vcard("handshake", "Client Relationships", "Long-standing client relationships built on trust and consistent delivery of results, case after case."),
            vcard("trophy", "Industry Recognition", "Our case work has contributed to multiple industry awards recognising our expertise and innovation.")
        ],
        "Discuss Your Case",
        "Talk to Us About Your Needs"),
    "Have a complex case? Contact us to see how we can help."
)

# 21. CONTACT US
make_page("contact-us.html", "Contact Us",
    "Contact Rainstone Money for expert mortgage and commercial finance advice. London and Luton offices. Call 020 7036 6435 or complete our enquiry form.",
    hero_html("Get in Touch",
        'Contact <em class="text-gold-italic">Us</em>',
        "We're Here to Help",
        'London &amp; Luton offices <span class="gold-dot">&middot;</span> Free consultations <span class="gold-dot">&middot;</span> Expert advice'),
    solutions_html("CONTACT US", "Let's Start the", "Conversation",
        "How to Reach Us",
        [
            "Whether you have a question about mortgages, commercial finance, insurance, or any of our services, we're here to help. Our friendly team is available by phone, email, or in person at our London and Luton offices.",
            "For a free initial consultation, simply call us on 020 7036 6435 or complete the enquiry form below. One of our expert advisors will get back to you within 24 hours to discuss your requirements.",
            "We offer appointments during business hours and can also arrange evening and weekend consultations by prior arrangement to work around your schedule."
        ],
        [
            scard("map-marker-alt", "London Office", "The Whitechapel Centre", "85 Myrdle Street, London E1 1HL. Our head office in the heart of East London, easily accessible by public transport."),
            scard("map-marker-alt", "Luton Office", "243D Dunstable Road", "Luton, LU4 8BW. Our Bedfordshire office serving clients across the Home Counties and Midlands."),
            scard("phone-alt", "Call Us", "020 7036 6435", "Speak directly to one of our expert advisors for immediate guidance and to book your free consultation.")
        ],
        [
            vcard("clock", "Quick Response", "We aim to respond to all enquiries within 24 hours, often much sooner during business hours."),
            vcard("gift", "Free Consultation", "Your initial consultation is completely free and comes with no obligation to proceed."),
            vcard("comments", "Clear Communication", "We explain everything in plain English, ensuring you understand your options before making any decisions."),
            vcard("user-tie", "Personal Service", "Every client is assigned a dedicated advisor who takes personal responsibility for their case.")
        ],
        "Send Us a Message",
        "Call 020 7036 6435"),
    "We'd love to hear from you. Complete the form below or call us directly."
)

# 22. PRIVACY POLICY
make_page("privacy-policy.html", "Privacy Policy",
    "Rainstone Money privacy policy. How we collect, use, and protect your personal data. Authorised and regulated by the FCA, Registration Number 743879.",
    hero_html("Your Privacy Matters",
        'Privacy <em class="text-gold-italic">Policy</em>',
        "Protecting Your Data",
        'FCA regulated <span class="gold-dot">&middot;</span> Data protection <span class="gold-dot">&middot;</span> Your rights'),
    solutions_html("PRIVACY POLICY", "How We Protect", "Your Data",
        "Our Commitment to Privacy",
        [
            "Rainstone Financial Services Limited (trading as Rainstone Money) is committed to protecting your privacy. This policy explains how we collect, use, store, and protect your personal information in accordance with the UK General Data Protection Regulation (UK GDPR) and the Data Protection Act 2018.",
            "We are authorised and regulated by the Financial Conduct Authority (FCA), Registration Number: 743879. As a regulated firm, we take our data protection obligations extremely seriously and have robust procedures in place to safeguard your information.",
            "We collect personal information that you provide directly to us, including your name, contact details, financial information, and employment details. This information is used solely for the purpose of providing you with financial advice and arranging financial products on your behalf."
        ],
        [
            scard("lock", "Data Security", "Your data is safe", "We employ industry-standard security measures including encryption, secure servers, and access controls to protect your personal information from unauthorised access."),
            scard("eye-slash", "Limited Access", "Need-to-know basis", "Your personal data is only accessed by authorised personnel who need it to provide you with our services. We never share data unnecessarily."),
            scard("user-shield", "Your Rights", "Control your data", "You have the right to access, correct, delete, or port your personal data at any time. Contact us to exercise any of these rights.")
        ],
        [
            vcard("shield-halved", "FCA Regulated", "As an FCA-regulated firm, we comply with all regulatory requirements regarding the handling and protection of client data."),
            vcard("file-alt", "Transparent Policies", "We are open about how we use your data and will always explain our processing activities clearly and in plain English."),
            vcard("clock", "Data Retention", "We only retain your personal data for as long as necessary to fulfil the purposes for which it was collected, in line with regulatory requirements."),
            vcard("phone-alt", "Contact Us", "If you have any questions about our privacy practices or wish to exercise your data rights, please contact us at info@rainstonemoney.co.uk.")
        ],
        "Contact Us About Your Data",
        "Email Us"),
    "Questions about your data? Contact our data protection team at info@rainstonemoney.co.uk."
)

# 23. MORTGAGE CALCULATOR
make_page("mortgage-calculator.html", "Mortgage Calculator",
    "Free mortgage calculator from Rainstone Money. Calculate your monthly repayments for interest-only and repayment mortgages. Get an instant estimate.",
    hero_html("Calculate Your Repayments",
        'Mortgage <em class="text-gold-italic">Calculator</em>',
        "Plan Your Borrowing",
        'Instant estimates <span class="gold-dot">&middot;</span> Interest-only &amp; repayment <span class="gold-dot">&middot;</span> Free to use'),
    solutions_html("MORTGAGE CALCULATOR", "Work Out Your Monthly", "Payments",
        "Free Mortgage Calculator",
        [
            "Use our free mortgage calculator to get an instant estimate of your monthly mortgage repayments. Simply enter your mortgage amount, term, and interest rate to see calculations for both interest-only and repayment mortgages.",
            "This calculator provides a helpful guide to understanding what your mortgage payments might look like. However, actual rates and terms will depend on your individual circumstances, the lender, and the specific product you choose.",
            "For a personalised mortgage quote based on your exact situation, contact our expert advisors who can search the whole market to find you the best deal."
        ],
        [
            scard("calculator", "Interest Only", "Lower monthly payments", "Calculate your monthly payments on an interest-only basis, where you only pay the interest each month and repay the capital at the end of the term."),
            scard("chart-line", "Capital Repayment", "Pay off your mortgage", "See what your payments would be on a repayment mortgage, where each monthly payment reduces both the interest and the capital owed."),
            scard("percent", "Rate Comparison", "Compare different rates", "Try different interest rates to see how they affect your monthly payments and total cost over the life of the mortgage.")
        ],
        [
            vcard("bolt", "Instant Results", "Get your calculation immediately. No need to provide personal details or create an account to use our calculator."),
            vcard("shield-halved", "General Guide Only", "This calculator provides estimates for guidance purposes. For accurate figures tailored to you, speak to one of our advisors."),
            vcard("phone-alt", "Expert Advice", "Once you've seen your estimate, our mortgage experts can search the whole market to find the best rates for your circumstances."),
            vcard("gift", "Free Service", "Our calculator is completely free to use, and our initial mortgage consultations are also offered at no charge.")
        ],
        "Get a Personalised Quote",
        "Speak to an Advisor"),
    "Want an accurate quote? Contact our mortgage experts for a personalised assessment."
)

print("\nAll pages generated successfully!")
