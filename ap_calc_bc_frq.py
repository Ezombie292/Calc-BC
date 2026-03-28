#!/usr/bin/env python3
"""
AP Calculus BC — FRQ Perfect-Credit Reference Tool
===================================================
Every FRQ type, every unit, with EXACT formatting for full credit.

Run:  python3 ap_calc_bc_frq.py
"""

import os, sys, textwrap

# ─────────────────────────────────────────────────────────
# Color helpers for terminal
# ─────────────────────────────────────────────────────────
BOLD = "\033[1m"
UL = "\033[4m"
RESET = "\033[0m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
DIM = "\033[2m"


def title(s):
    return f"\n{BOLD}{CYAN}{'═'*60}\n  {s}\n{'═'*60}{RESET}\n"


def section(s):
    return f"\n{BOLD}{GREEN}── {s} ──{RESET}\n"


def warn(s):
    return f"{YELLOW}⚠  {s}{RESET}"


def tip(s):
    return f"{MAGENTA}★  {s}{RESET}"


def example(s):
    return f"{DIM}{s}{RESET}"


# ─────────────────────────────────────────────────────────
# GLOBAL FORMATTING RULES  (apply to EVERY FRQ)
# ─────────────────────────────────────────────────────────
GLOBAL_RULES = f"""
{title("UNIVERSAL FRQ FORMATTING RULES — MEMORIZE THESE")}

{section("1. LABELING")}
  • Label EVERY part (a), (b), (c), (d) clearly.
  • If a part has sub-parts, label those too: (i), (ii).
  • {warn("If you answer (b) on the page for (a), CLEARLY indicate it.")}

{section("2. SHOW SETUP, NOT JUST ANSWER")}
  • Write the integral/derivative/equation BEFORE evaluating.
  • {tip("Setup points are often 1 pt; answer is another 1 pt. You can get partial credit.")}

  {BOLD}Example — Definite Integral:{RESET}
    ∫₀⁵ f(x) dx = F(5) − F(0) = 17 − 3 = 14

  {BOLD}Example — Derivative:{RESET}
    f'(x) = 3x² − 4x + 1
    f'(2) = 3(4) − 4(2) + 1 = 5

{section("3. UNITS")}
  • {RED}{BOLD}ALWAYS include units when the problem has a context/real-world scenario.{RESET}
  • Derivative units: [output unit] / [input unit]
      e.g., gallons/minute, feet/sec², dollars/item
  • Integral units: [integrand unit] × [variable unit]
      e.g., (gallons/min)(min) = gallons
  • {warn("Missing units = lost point. It's almost always 1 pt just for units.")}

{section("4. DECIMAL ANSWERS")}
  • Store full values in your calculator; only round at the FINAL answer.
  • Round to 3 decimal places (or truncate to 3) unless told otherwise.
  • {warn("DO NOT round intermediate steps. 1.3456 × 2.789 ≠ 1.346 × 2.789")}
  • Acceptable: 4.132 or 4.133 (both fine for truncate vs round)

{section("5. JUSTIFICATION LANGUAGE")}
  The AP exam requires SPECIFIC phrases. Using the wrong word = 0 pts.

  {BOLD}For extrema (relative max/min):{RESET}
    "f'(x) changes from positive to negative at x = c,
     so f has a relative maximum at x = c."
    {warn("Do NOT say 'f(x) changes from increasing to decreasing.' — that's informal.")}
    {warn("Do NOT say 'the slope is 0 so it's a max.' — f'=0 alone is not sufficient.")}

  {BOLD}For absolute extrema on [a,b]:{RESET}
    "Comparing f(a), f(critical points), and f(b):
     f(c) = 12 is the largest value, so the absolute maximum of f on [a,b] is 12."
    {tip("You MUST evaluate f at endpoints AND critical points. State the comparison.")}

  {BOLD}For increasing/decreasing:{RESET}
    "f'(x) > 0 on (a, b), so f is increasing on (a, b)."
    {warn("Say 'f is increasing' not 'f(x) is going up'.")}

  {BOLD}For concavity:{RESET}
    "f''(x) > 0 on (a, b), so f is concave up on (a, b)."
    "f''(x) changes sign at x = c, so f has a point of inflection at x = c."

  {BOLD}For continuity (in limit/IVT problems):{RESET}
    "f is continuous on [a, b] because [reason]."
    {warn("You MUST state continuity before applying IVT or EVT.")}

{section("6. CROSSING OUT WORK")}
  • Neatly cross out (single line through) incorrect work.
  • Graders score what is NOT crossed out.
  • {warn("If you leave two answers and don't cross one out, they grade the WORSE one.")}

{section("7. CALCULATOR vs. NON-CALCULATOR")}
  • FRQs 1–2: calculator allowed
  • FRQs 3–6: NO calculator
  • On calculator sections: you still must write the setup.
    e.g., "∫₁⁴ √(1 + (f'(x))²) dx = 7.341"  ← write the integral, then the value.
  • On non-calculator: show all algebraic/arithmetic steps.
"""

# ─────────────────────────────────────────────────────────
# UNITS — indexed by topic
# ─────────────────────────────────────────────────────────

UNITS = {}

UNITS[1] = f"""
{title("UNIT 1 — LIMITS AND CONTINUITY")}

{section("FRQ Type: Continuity / Removable Discontinuity")}

  {BOLD}Question pattern:{RESET}
  "Is f continuous at x = c? Justify."

  {BOLD}PERFECT-CREDIT FORMAT:{RESET}

    (1) State the three conditions:
        (i)  f(c) is defined.        → f(c) = [value]
        (ii) lim(x→c) f(x) exists.  → lim(x→c⁻) f(x) = [value]
                                        lim(x→c⁺) f(x) = [value]
                                        Since both = [value], lim(x→c) f(x) = [value].
        (iii) lim(x→c) f(x) = f(c). → [value] = [value]  ✓

    (2) Conclude:
        "Since all three conditions are met, f is continuous at x = c."

    OR if NOT continuous:
        "Since lim(x→c) f(x) = 5 ≠ 3 = f(c), f is NOT continuous at x = c."

  {warn("You MUST check all three conditions. Saying 'the limit equals f(c)' without")}
  {warn("first establishing that both exist is incomplete.")}

{section("FRQ Type: Intermediate Value Theorem (IVT)")}

  {BOLD}Question pattern:{RESET}
  "Must there be a value c in [a,b] where f(c) = k?"

  {BOLD}PERFECT-CREDIT FORMAT:{RESET}

    (1) "f is continuous on [a, b] because [it is a polynomial / given / etc.]."
    (2) "f(a) = [value] and f(b) = [value]."
    (3) "Since f(a) < k < f(b) [or f(b) < k < f(a)],
         by the Intermediate Value Theorem, there exists at least one
         value c in (a, b) such that f(c) = k."

  {warn("You MUST state that f is continuous AND give the reason.")}
  {warn("You MUST show that k is BETWEEN f(a) and f(b).")}
  {tip("If they give a table, cite the specific table values.")}

{section("FRQ Type: Squeeze Theorem")}

  {BOLD}PERFECT-CREDIT FORMAT:{RESET}

    (1) "g(x) ≤ f(x) ≤ h(x) for all x near c."
    (2) "lim(x→c) g(x) = L and lim(x→c) h(x) = L."
    (3) "By the Squeeze Theorem, lim(x→c) f(x) = L."
"""

UNITS[2] = f"""
{title("UNIT 2 — DIFFERENTIATION: DEFINITION & BASIC RULES")}

{section("FRQ Type: Limit Definition of Derivative")}

  {BOLD}Question pattern:{RESET}
  "Use the definition of the derivative to find f'(a)."

  {BOLD}PERFECT-CREDIT FORMAT:{RESET}

    f'(a) = lim(h→0) [f(a+h) − f(a)] / h

    OR equivalently:

    f'(a) = lim(x→a) [f(x) − f(a)] / (x − a)

    Then: substitute, simplify, evaluate limit.

  {tip("Show EVERY algebraic step. Don't skip the factoring.")}

{section("FRQ Type: Differentiability implies Continuity")}

  {BOLD}Question pattern:{RESET}
  "Is f differentiable at x = c?"

  {BOLD}PERFECT-CREDIT FORMAT:{RESET}

    Check that:
    (1) f is continuous at x = c  (left limit = right limit = f(c))
    (2) lim(h→0⁻) [f(c+h)−f(c)]/h = lim(h→0⁺) [f(c+h)−f(c)]/h

    "The left-hand derivative = [value] and the right-hand derivative = [value].
     Since [they are equal / they are NOT equal], f [is / is not] differentiable at x = c."

  {warn("If f is not continuous at c, f is automatically not differentiable.")}
  {warn("A corner, cusp, or vertical tangent means NOT differentiable.")}

{section("FRQ Type: Tangent Line / Linear Approximation")}

  {BOLD}Question pattern:{RESET}
  "Write the equation of the tangent line at x = a. Use it to approximate f(b)."

  {BOLD}PERFECT-CREDIT FORMAT:{RESET}

    (1) Find slope: f'(a) = [value]
    (2) Find point: f(a) = [value]
    (3) Tangent line: y − f(a) = f'(a)(x − a)
                  OR: y = f(a) + f'(a)(x − a)

    (4) Approximation: f(b) ≈ f(a) + f'(a)(b − a) = [value]

    (5) If asked whether overestimate or underestimate:
        "Since f''(x) [> 0 / < 0] on an interval containing a and b,
         f is concave [up / down], so the tangent line is
         [below / above] the curve, making this an [under / over]estimate."

  {tip("Concave UP → tangent line BELOW curve → UNDERESTIMATE")}
  {tip("Concave DOWN → tangent line ABOVE curve → OVERESTIMATE")}
"""

UNITS[3] = f"""
{title("UNIT 3 — DIFFERENTIATION: COMPOSITE, IMPLICIT, INVERSE")}

{section("FRQ Type: Chain Rule in Context")}

  {BOLD}Question pattern:{RESET}
  "Given g(x) = f(h(x)), find g'(a)."  (Often uses a table of values.)

  {BOLD}PERFECT-CREDIT FORMAT:{RESET}

    g'(x) = f'(h(x)) · h'(x)
    g'(a) = f'(h(a)) · h'(a)
           = f'([value from table]) · [value from table]
           = [number] · [number]
           = [answer]

  {tip("Write the Chain Rule formula FIRST, then substitute. Setup point + answer point.")}

{section("FRQ Type: Implicit Differentiation")}

  {BOLD}Question pattern:{RESET}
  "Given an equation, find dy/dx. Then find the tangent line, or where tangent is horizontal/vertical."

  {BOLD}PERFECT-CREDIT FORMAT — finding dy/dx:{RESET}

    (1) Differentiate both sides with respect to x:
        d/dx[left side] = d/dx[right side]

    (2) Every time you differentiate a y-term, attach dy/dx.

    (3) Collect all dy/dx terms on one side, factor out dy/dx, solve:
        dy/dx = [expression in x and y]

  {BOLD}Horizontal tangent:{RESET}
    "dy/dx = 0 when [numerator] = 0, provided [denominator] ≠ 0."
    Solve numerator = 0 for relationship, substitute back into ORIGINAL equation.

  {BOLD}Vertical tangent:{RESET}
    "dy/dx is undefined when [denominator] = 0, provided [numerator] ≠ 0."
    Same process: solve denominator = 0, substitute back.

  {warn("After finding x (or y), you MUST find the OTHER coordinate from the original equation.")}
  {warn("You must verify the denominator ≠ 0 (for horizontal) or numerator ≠ 0 (for vertical).")}

{section("FRQ Type: Derivative of Inverse Function")}

  {BOLD}Question pattern:{RESET}
  "If g is the inverse of f, find g'(a)."

  {BOLD}PERFECT-CREDIT FORMAT:{RESET}

    g'(a) = 1 / f'(g(a))

    Step 1: Find g(a).  Since g = f⁻¹, g(a) = b means f(b) = a.
            Look up in table: f(b) = a  →  b = [value]
    Step 2: Find f'(b) = [value from table or computation]
    Step 3: g'(a) = 1 / f'(b) = 1 / [value] = [answer]

  {warn("The most common error: using f'(a) instead of f'(g(a)). Be careful!")}
"""

UNITS[4] = f"""
{title("UNIT 4 — CONTEXTUAL APPLICATIONS OF DIFFERENTIATION")}

{section("FRQ Type: Rates of Change / Interpretation of Derivative")}

  {BOLD}Question pattern:{RESET}
  "What is the meaning of f'(t) in context?"  or  "Interpret f'(3) = −2."

  {BOLD}PERFECT-CREDIT FORMAT:{RESET}

    "At time t = 3 [units of t], the [quantity described by f] is
     [decreasing/increasing] at a rate of [|f'(3)|] [units of f] per [unit of t]."

  {BOLD}Concrete example:{RESET}
    If W(t) = gallons of water and t = minutes, and W'(3) = −2:

    "At time t = 3 minutes, the amount of water in the tank is
     decreasing at a rate of 2 gallons per minute."

  {warn("Say 'decreasing at a rate of 2' NOT 'changing at a rate of −2'.")}
  {warn("Include UNITS. Include the SPECIFIC TIME. Include the CONTEXT.")}
  {tip("Three things graders check: (1) units (2) context language (3) 'at time t = __'")}

{section("FRQ Type: Related Rates")}

  {BOLD}Question pattern:{RESET}
  "At what rate is [quantity] changing when [conditions]?"

  {BOLD}PERFECT-CREDIT FORMAT:{RESET}

    (1) Define variables with units:
        "Let r = radius (cm), V = volume (cm³), t = time (sec)."

    (2) Write the equation relating the variables:
        V = (4/3)πr³

    (3) Differentiate BOTH sides with respect to t:
        dV/dt = 4πr² · (dr/dt)

    (4) Substitute known values:
        dV/dt = 4π(5)²(3) = 300π

    (5) Answer with units:
        "The volume is increasing at a rate of 300π cm³/sec."

  {warn("Differentiate with respect to TIME, not with respect to x or r.")}
  {warn("Don't substitute values BEFORE differentiating.")}
  {tip("Label known vs. unknown rates BEFORE you start.")}

{section("FRQ Type: L'Hôpital's Rule  (BC ONLY)")}

  {BOLD}PERFECT-CREDIT FORMAT:{RESET}

    (1) "lim(x→c) f(x)/g(x) is of the form 0/0 [or ∞/∞]."
    (2) "By L'Hôpital's Rule:
         lim(x→c) f(x)/g(x) = lim(x→c) f'(x)/g'(x) = [value]."

  {warn("You MUST state that the limit is in indeterminate form FIRST.")}

{section("FRQ Type: Motion Along a Line (Position, Velocity, Acceleration)")}

  {BOLD}Key relationships:{RESET}
    Position: s(t) or x(t)
    Velocity: v(t) = s'(t)
    Speed:    |v(t)|
    Acceleration: a(t) = v'(t) = s''(t)

  {BOLD}"Is the particle speeding up or slowing down at t = c?"{RESET}

    "v(c) = [value] and a(c) = [value].
     Since v(c) and a(c) have [the same sign / opposite signs],
     the particle is [speeding up / slowing down] at t = c."

  {tip("Same signs → speeding up.  Opposite signs → slowing down.")}
  {warn("Speed ≠ velocity. Speed = |v(t)|. Don't confuse them.")}

  {BOLD}"What is the total distance traveled on [a,b]?"{RESET}

    ∫ₐᵇ |v(t)| dt

    {tip("Use absolute value of velocity. Split into intervals where v changes sign if no calculator.")}

  {BOLD}"What is the displacement on [a,b]?"{RESET}

    ∫ₐᵇ v(t) dt = s(b) − s(a)

    {tip("Displacement uses v(t) without absolute value.")}
"""

UNITS[5] = f"""
{title("UNIT 5 — ANALYTICAL APPLICATIONS OF DIFFERENTIATION")}

{section("FRQ Type: First Derivative Test for Extrema")}

  {BOLD}PERFECT-CREDIT FORMAT:{RESET}

    "f'(x) = 0 at x = c.
     f'(x) changes from [positive to negative / negative to positive] at x = c.
     Therefore, f has a [relative maximum / relative minimum] at x = c."

  {warn("You MUST say 'f' changes from pos to neg' — don't just say f'(c)=0.")}
  {warn("f'(c) = 0 alone is NOT a justification. The SIGN CHANGE is what matters.")}

{section("FRQ Type: Second Derivative Test for Extrema")}

  {BOLD}PERFECT-CREDIT FORMAT:{RESET}

    "f'(c) = 0 and f''(c) = [positive/negative number].
     Since f'(c) = 0 and f''(c) [> 0 / < 0], f has a
     [relative minimum / relative maximum] at x = c."

  {tip("f''(c) > 0 → concave UP → relative MINIMUM (cup holds water = min)")}
  {tip("f''(c) < 0 → concave DOWN → relative MAXIMUM")}

{section("FRQ Type: Candidates Test (Absolute Extrema on Closed Interval)")}

  {BOLD}Question pattern:{RESET}
  "Find the absolute maximum/minimum of f on [a, b]."

  {BOLD}PERFECT-CREDIT FORMAT:{RESET}

    (1) Find critical points: f'(x) = 0 or f'(x) DNE in (a,b).
    (2) Evaluate f at each critical point AND at the endpoints:
        f(a) = ___
        f(c₁) = ___
        f(c₂) = ___
        f(b) = ___
    (3) "The absolute maximum of f on [a,b] is [largest value] at x = [x-value].
         The absolute minimum of f on [a,b] is [smallest value] at x = [x-value]."

  {warn("You MUST evaluate at ENDPOINTS, not just critical points.")}
  {warn("State the VALUE, not just the x-coordinate.")}

{section("FRQ Type: Mean Value Theorem (MVT)")}

  {BOLD}Question pattern:{RESET}
  "Does MVT guarantee a value c where f'(c) = [some rate]?"

  {BOLD}PERFECT-CREDIT FORMAT:{RESET}

    (1) "f is continuous on [a, b] and differentiable on (a, b) because [reason]."
    (2) "By the Mean Value Theorem, there exists at least one c in (a, b) such that:
         f'(c) = [f(b) − f(a)] / (b − a) = [value]."

  {warn("MUST state both continuous on [a,b] AND differentiable on (a,b).")}

{section("FRQ Type: Inflection Points")}

  {BOLD}PERFECT-CREDIT FORMAT:{RESET}

    "f''(x) changes sign at x = c
     [from positive to negative / from negative to positive],
     so f has a point of inflection at x = c."

  {warn("f''(c) = 0 alone does NOT mean inflection. The SIGN CHANGE of f'' is required.")}

{section("FRQ Type: Graph of f' → properties of f")}

  This is one of the MOST COMMON FRQ types. You're given a graph of f' and asked about f.

  {BOLD}Reading the graph of f':{RESET}
    • f' > 0 (above x-axis)  → f is increasing
    • f' < 0 (below x-axis)  → f is decreasing
    • f' = 0 (crosses x-axis) → possible extremum of f
    • f' changes + to −  → f has relative maximum
    • f' changes − to +  → f has relative minimum
    • f' increasing → f'' > 0 → f is concave up
    • f' decreasing → f'' < 0 → f is concave down
    • f' has a local extremum → f'' = 0 → possible inflection point of f

  {tip("When f' has a RELATIVE MAX or MIN, f has an INFLECTION POINT (if f'' changes sign there).")}
"""

UNITS[6] = f"""
{title("UNIT 6 — INTEGRATION AND ACCUMULATION OF CHANGE")}

{section("FRQ Type: Accumulation Function / FTC Part 1")}

  {BOLD}Question pattern:{RESET}
  "Let g(x) = ∫ₐˣ f(t) dt.  Find g'(x), g''(x), etc."

  {BOLD}PERFECT-CREDIT FORMAT:{RESET}

    By the Fundamental Theorem of Calculus:
    g'(x) = f(x)

    If the upper limit is a function:
    g(x) = ∫ₐ^(h(x)) f(t) dt
    g'(x) = f(h(x)) · h'(x)     ← Chain Rule!

  {tip("g'(x) = f(x) means: the graph of f IS the graph of g'.")}
  {tip("g''(x) = f'(x), so the slope of the f graph gives concavity of g.")}

{section("FRQ Type: Definite Integral as Net Change")}

  {BOLD}Question pattern:{RESET}
  "Given r(t) = rate of [something]. Find the total [something] from t=a to t=b."

  {BOLD}PERFECT-CREDIT FORMAT:{RESET}

    "The total [quantity] from t = a to t = b is:
     ∫ₐᵇ r(t) dt = [value] [units]."

  {BOLD}If there's an initial condition:{RESET}
    "Q(b) = Q(a) + ∫ₐᵇ r(t) dt = [initial] + [integral value] = [answer] [units]."

  {warn("∫ r(t) dt gives the NET change, not the total amount.")}
  {warn("For total amount: initial value + net change.")}

{section("FRQ Type: Average Value of a Function")}

  {BOLD}PERFECT-CREDIT FORMAT:{RESET}

    "The average value of f on [a, b] is:
     (1/(b−a)) ∫ₐᵇ f(x) dx = (1/[b−a]) · [integral value] = [answer]"

  {tip("Don't forget the 1/(b−a) out front!")}
  {warn("Include UNITS if contextual.")}

{section("FRQ Type: Riemann Sums (from table)")}

  {BOLD}Question pattern:{RESET}
  "Use a left/right/midpoint/trapezoidal sum with n subintervals to approximate ∫ₐᵇ f(x) dx."

  {BOLD}PERFECT-CREDIT FORMAT — Left Riemann Sum:{RESET}
    ∫ₐᵇ f(x) dx ≈ Σ f(xᵢ) · Δxᵢ
    = f(x₀)(x₁−x₀) + f(x₁)(x₂−x₁) + f(x₂)(x₃−x₂) + ...
    = [show each term] = [answer]

  {BOLD}Trapezoidal Sum:{RESET}
    ≈ Σ [(f(xᵢ) + f(xᵢ₊₁))/2] · Δxᵢ
    = [(f(x₀)+f(x₁))/2](x₁−x₀) + [(f(x₁)+f(x₂))/2](x₂−x₁) + ...
    = [show each term] = [answer]

  {warn("Subintervals may NOT be equal width! Use each Δxᵢ = xᵢ₊₁ − xᵢ separately.")}

  {BOLD}"Is this an overestimate or underestimate?"{RESET}

    Left sum on INCREASING function  → UNDERESTIMATE
    Left sum on DECREASING function  → OVERESTIMATE
    Right sum on INCREASING function → OVERESTIMATE
    Right sum on DECREASING function → UNDERESTIMATE
    Trapezoidal on CONCAVE UP        → OVERESTIMATE
    Trapezoidal on CONCAVE DOWN      → UNDERESTIMATE

    "Since f is [increasing/concave up/etc.] on [a,b], the [type] sum is an
     [over/under]estimate of ∫ₐᵇ f(x) dx."
"""

UNITS[7] = f"""
{title("UNIT 7 — DIFFERENTIAL EQUATIONS")}

{section("FRQ Type: Slope Fields")}

  {BOLD}Question pattern:{RESET}
  "Sketch the slope field" or "Describe the slope field at given points."

  {BOLD}PERFECT-CREDIT FORMAT (matching a solution to a slope field):{RESET}
    "The solution curve passes through (x₀, y₀) and follows the direction
     of the slope segments."

  {tip("Check: where is dy/dx = 0? (horizontal segments)")}
  {tip("Check: where is dy/dx undefined? (vertical/no segments)")}
  {tip("Check: does dy/dx depend on only x, only y, or both?")}

{section("FRQ Type: Euler's Method  (BC ONLY)")}

  {BOLD}Question pattern:{RESET}
  "Use Euler's method with step size Δx to approximate f(x₀ + nΔx)."

  {BOLD}PERFECT-CREDIT FORMAT:{RESET}

    Given: dy/dx = F(x,y), initial point (x₀, y₀), step size Δx.

    Step 1: (x₀, y₀)
            dy/dx at (x₀, y₀) = F(x₀, y₀) = m₀
            y₁ = y₀ + m₀ · Δx = [value]
            New point: (x₁, y₁) = (x₀ + Δx, y₁)

    Step 2: (x₁, y₁)
            dy/dx at (x₁, y₁) = F(x₁, y₁) = m₁
            y₂ = y₁ + m₁ · Δx = [value]
            New point: (x₂, y₂) = (x₁ + Δx, y₂)

    [Continue for required steps...]

    "Using Euler's method, f([final x]) ≈ [final y value]."

  {warn("Show EVERY step. Each step is usually worth a point.")}
  {tip("Make a table: xₙ | yₙ | dy/dx | yₙ₊₁ = yₙ + (dy/dx)·Δx")}

{section("FRQ Type: Separation of Variables")}

  {BOLD}Question pattern:{RESET}
  "Find the particular solution to the differential equation."

  {BOLD}PERFECT-CREDIT FORMAT:{RESET}

    Given: dy/dx = [expression in x and y], y(x₀) = y₀

    (1) Separate variables:
        [y-stuff] dy = [x-stuff] dx

    (2) Integrate both sides:
        ∫ [y-stuff] dy = ∫ [x-stuff] dx
        [antiderivative of y side] = [antiderivative of x side] + C

    (3) Use initial condition to find C:
        Substitute (x₀, y₀): solve for C.

    (4) Solve for y (if requested):
        y = [explicit function of x]

  {warn("Don't forget the +C on ONE side (not both).")}
  {warn("Use the initial condition AFTER integrating, not before.")}
  {warn("If you can't solve for y explicitly, leave it in implicit form.")}
  {tip("Write +C immediately when you integrate. Forgetting it = lost point.")}

{section("FRQ Type: Logistic Growth  (BC ONLY)")}

  {BOLD}The equation:{RESET}
    dP/dt = kP(1 − P/L)    where L = carrying capacity

  {BOLD}Key facts (all commonly tested):{RESET}
    • Solution: P(t) = L / (1 + Ae^(−kt))  where A = (L − P₀)/P₀
    • Maximum growth rate occurs at P = L/2
    • As t → ∞, P → L (carrying capacity)
    • P = L/2 is the inflection point of the logistic curve

  {BOLD}"At what population is the growth rate maximized?"{RESET}
    "The growth rate dP/dt is maximized when P = L/2 = [value]."

  {warn("Know the formula AND the conceptual properties.")}
"""

UNITS[8] = f"""
{title("UNIT 8 — APPLICATIONS OF INTEGRATION")}

{section("FRQ Type: Area Between Curves")}

  {BOLD}PERFECT-CREDIT FORMAT:{RESET}

    "The area between f(x) and g(x) from x = a to x = b is:
     A = ∫ₐᵇ |f(x) − g(x)| dx"

    In practice (when you know which is on top):
     A = ∫ₐᵇ [top − bottom] dx     (for vertical slices)
     A = ∫_c^d [right − left] dy    (for horizontal slices)

  {warn("ALWAYS state which function is greater: 'Since f(x) ≥ g(x) on [a,b]...'")}
  {warn("If the curves cross, SPLIT the integral at the intersection.")}

  {BOLD}Finding intersection points:{RESET}
    "Setting f(x) = g(x): [solve]. The curves intersect at x = ..."

{section("FRQ Type: Volume — Disk/Washer Method")}

  {BOLD}Disk (no hole):{RESET}
    V = π ∫ₐᵇ [R(x)]² dx
    where R(x) = distance from curve to axis of rotation

  {BOLD}Washer (with hole):{RESET}
    V = π ∫ₐᵇ ([R(x)]² − [r(x)]²) dx
    R(x) = outer radius, r(x) = inner radius

  {BOLD}PERFECT-CREDIT FORMAT:{RESET}
    "Rotating about [axis]:
     R(x) = [outer function − axis] = [expression]
     r(x) = [inner function − axis] = [expression]
     V = π ∫ₐᵇ ([R(x)]² − [r(x)]²) dx = π ∫ₐᵇ ([expr]² − [expr]²) dx = [value]"

  {warn("For rotation about y = k: R = k − f(x) or f(x) − k (whichever is positive).")}
  {warn("For rotation about x = k: use the shell method or switch to dy.")}
  {tip("Draw the radius lines from the axis to the curve to visualize.")}

{section("FRQ Type: Volume — Cross Sections")}

  {BOLD}PERFECT-CREDIT FORMAT:{RESET}

    "The base is the region between f(x) and g(x). Cross sections
     perpendicular to the x-axis are [squares / semicircles / equilateral triangles / etc.]."

    Side length s(x) = f(x) − g(x)   (the distance between curves)

    Square:               A(x) = s² = [f(x) − g(x)]²
    Semicircle:           A(x) = (π/8)s² = (π/8)[f(x) − g(x)]²
    Equilateral triangle: A(x) = (√3/4)s² = (√3/4)[f(x) − g(x)]²
    Isosceles right (leg): A(x) = (1/2)s²
    Isosceles right (hyp): A(x) = (1/4)s²

    V = ∫ₐᵇ A(x) dx

  {warn("Write the area formula BEFORE integrating. That's a setup point.")}
  {tip("Memorize: semicircle area = (π/8)d² where d = diameter (the cross-section side).")}

{section("FRQ Type: Arc Length  (BC ONLY)")}

  {BOLD}PERFECT-CREDIT FORMAT:{RESET}

    For y = f(x) from x = a to x = b:
    L = ∫ₐᵇ √(1 + [f'(x)]²) dx

    For parametric x = x(t), y = y(t) from t = a to t = b:
    L = ∫ₐᵇ √([x'(t)]² + [y'(t)]²) dt

  {tip("This is almost always a calculator problem. Write the integral, then evaluate.")}
"""

UNITS[9] = f"""
{title("UNIT 9 — PARAMETRIC, POLAR, AND VECTOR-VALUED FUNCTIONS  (BC ONLY)")}

{section("FRQ Type: Parametric Curves — dy/dx and d²y/dx²")}

  {BOLD}PERFECT-CREDIT FORMAT — First derivative:{RESET}

    dy/dx = (dy/dt) / (dx/dt) = y'(t) / x'(t)

  {BOLD}PERFECT-CREDIT FORMAT — Second derivative:{RESET}

    d²y/dx² = (d/dt)[dy/dx] / (dx/dt)

    Step 1: Compute dy/dx = y'(t)/x'(t)
    Step 2: Take d/dt of that result (use quotient rule)
    Step 3: Divide by dx/dt

  {warn("d²y/dx² is NOT y''(t)/x''(t). This is the #1 parametric mistake.")}
  {warn("d²y/dx² = [d/dt(dy/dx)] / [dx/dt]")}

{section("FRQ Type: Parametric — Speed and Distance")}

  {BOLD}Speed at time t:{RESET}
    Speed = √([x'(t)]² + [y'(t)]²)

  {BOLD}Total distance traveled from t = a to t = b:{RESET}
    ∫ₐᵇ √([x'(t)]² + [y'(t)]²) dt

  {BOLD}PERFECT-CREDIT FORMAT:{RESET}
    "The speed of the particle at t = c is:
     √([x'(c)]² + [y'(c)]²) = √([value]² + [value]²) = [answer]"

  {tip("Speed is ALWAYS positive. It's the magnitude of the velocity vector.")}

{section("FRQ Type: Parametric — Tangent Lines")}

  {BOLD}Horizontal tangent:{RESET} dy/dt = 0 AND dx/dt ≠ 0
  {BOLD}Vertical tangent:{RESET} dx/dt = 0 AND dy/dt ≠ 0

  "dy/dt = 0 at t = [value], and dx/dt ≠ 0 at that t.
   So the curve has a horizontal tangent at t = [value]."

{section("FRQ Type: Vector-Valued Functions — Position, Velocity, Acceleration")}

  {BOLD}Key relationships:{RESET}
    Position:     r(t) = ⟨x(t), y(t)⟩
    Velocity:     v(t) = ⟨x'(t), y'(t)⟩
    Acceleration: a(t) = ⟨x''(t), y''(t)⟩

  {BOLD}"Find the position at time t = b given v(t) and position at t = a."{RESET}

    x(b) = x(a) + ∫ₐᵇ x'(t) dt
    y(b) = y(a) + ∫ₐᵇ y'(t) dt

    "The position at t = b is:
     (x(a) + ∫ₐᵇ x'(t) dt,  y(a) + ∫ₐᵇ y'(t) dt) = ([value], [value])"

{section("FRQ Type: Polar Curves — Area")}

  {BOLD}PERFECT-CREDIT FORMAT:{RESET}

    "The area enclosed by r = f(θ) from θ = α to θ = β is:
     A = (1/2) ∫_α^β [f(θ)]² dθ"

  {BOLD}Area between two polar curves:{RESET}
    A = (1/2) ∫_α^β ([R_outer]² − [R_inner]²) dθ

  {warn("Don't forget the 1/2 out front!")}
  {warn("Determine α and β by setting the two curves equal or analyzing the graph.")}
  {tip("If the problem says 'one petal of r = cos(3θ)', the bounds are where r = 0.")}

  {BOLD}Finding bounds for a petal:{RESET}
    r = 0  →  cos(3θ) = 0  →  3θ = π/2, 3π/2, ...
    One petal: θ = −π/6 to θ = π/6   (for the petal on the positive x-axis)

{section("FRQ Type: Polar — dy/dx")}

  {BOLD}PERFECT-CREDIT FORMAT:{RESET}

    x = r cos θ,  y = r sin θ

    dx/dθ = r'cos θ − r sin θ
    dy/dθ = r'sin θ + r cos θ

    dy/dx = (dy/dθ) / (dx/dθ)

  {warn("You need the product rule since both r and trig depend on θ.")}
"""

UNITS[10] = f"""
{title("UNIT 10 — INFINITE SEQUENCES AND SERIES  (BC ONLY)")}

{section("FRQ Type: Convergence Tests")}

  {BOLD}For EVERY series convergence question, state:{RESET}
  (1) Which test you are using.
  (2) Show the test's conditions are met.
  (3) State the conclusion.

  {BOLD}nth Term (Divergence) Test:{RESET}
    "lim(n→∞) aₙ = [nonzero value or DNE] ≠ 0.
     By the nth Term Test, the series diverges."
    {warn("This can ONLY prove divergence, NEVER convergence.")}

  {BOLD}Geometric Series: Σ arⁿ{RESET}
    "This is a geometric series with first term a = [value] and ratio r = [value].
     Since |r| = [value] < 1, the series converges to a/(1−r) = [value]."
    OR: "Since |r| = [value] ≥ 1, the series diverges."

  {BOLD}p-Series: Σ 1/nᵖ{RESET}
    "This is a p-series with p = [value].
     Since p [> 1 / ≤ 1], the series [converges / diverges]."

  {BOLD}Integral Test:{RESET}
    "Let f(x) = [corresponding function]. f is positive, continuous, and decreasing on [1, ∞).
     ∫₁^∞ f(x) dx = [value or ∞].
     By the Integral Test, the series [converges / diverges]."

  {BOLD}Direct Comparison Test:{RESET}
    "0 ≤ aₙ ≤ bₙ for all n ≥ N.
     Since Σ bₙ converges, by the Direct Comparison Test, Σ aₙ converges."
    OR:
    "0 ≤ bₙ ≤ aₙ for all n ≥ N.
     Since Σ bₙ diverges, by the Direct Comparison Test, Σ aₙ diverges."

  {BOLD}Limit Comparison Test:{RESET}
    "Let bₙ = [comparison series].
     lim(n→∞) aₙ/bₙ = L = [positive finite value].
     Since 0 < L < ∞ and Σ bₙ [converges/diverges],
     by the Limit Comparison Test, Σ aₙ [converges/diverges]."

  {BOLD}Ratio Test:{RESET}
    "lim(n→∞) |aₙ₊₁/aₙ| = L = [value].
     Since L [< 1 / > 1 / = 1], the series [converges absolutely / diverges / test is inconclusive]."

  {BOLD}Alternating Series Test:{RESET}
    "The series Σ (−1)ⁿ bₙ where bₙ > 0.
     (1) lim(n→∞) bₙ = 0  ✓
     (2) bₙ₊₁ ≤ bₙ for all n ≥ N (bₙ is eventually decreasing)  ✓
     By the Alternating Series Test, the series converges."

  {warn("MUST check BOTH conditions for AST.")}

{section("FRQ Type: Alternating Series Error Bound")}

  {BOLD}PERFECT-CREDIT FORMAT:{RESET}

    "By the Alternating Series Estimation Theorem,
     the error |S − Sₙ| ≤ |aₙ₊₁| = [value]."

    Or: "The first omitted term is aₙ₊₁ = [value].
     |error| ≤ |aₙ₊₁| = [value]."

  {tip("Error ≤ first OMITTED (unused) term.")}

{section("FRQ Type: Taylor / Maclaurin Series")}

  {BOLD}Key Maclaurin series (MEMORIZE):{RESET}

    eˣ = Σ xⁿ/n! = 1 + x + x²/2! + x³/3! + ...         (all x)

    sin x = Σ (−1)ⁿ x²ⁿ⁺¹/(2n+1)! = x − x³/3! + x⁵/5! − ...  (all x)

    cos x = Σ (−1)ⁿ x²ⁿ/(2n)! = 1 − x²/2! + x⁴/4! − ...      (all x)

    1/(1−x) = Σ xⁿ = 1 + x + x² + x³ + ...              (|x| < 1)

    ln(1+x) = Σ (−1)ⁿ⁺¹ xⁿ/n = x − x²/2 + x³/3 − ...  (−1 < x ≤ 1)

  {BOLD}PERFECT-CREDIT FORMAT — Taylor polynomial about x = a:{RESET}

    f(x) ≈ Pₙ(x) = f(a) + f'(a)(x−a) + f''(a)(x−a)²/2! + f'''(a)(x−a)³/3! + ...

    Show derivatives:
      f(a) = [value]
      f'(a) = [value]
      f''(a) = [value]
      f'''(a) = [value]

    Pₙ(x) = [value] + [value](x−a) + [value](x−a)²/2 + [value](x−a)³/6 + ...

  {warn("Don't forget to divide by n! — the coefficient of (x−a)ⁿ is f⁽ⁿ⁾(a)/n!")}

{section("FRQ Type: Lagrange Error Bound")}

  {BOLD}PERFECT-CREDIT FORMAT:{RESET}

    "The Lagrange error bound for the nth-degree Taylor polynomial is:
     |Rₙ(x)| ≤ M|x − a|ⁿ⁺¹ / (n+1)!

     where M = max|f⁽ⁿ⁺¹⁾(z)| for z between a and x.

     M = [value or bound]
     |Rₙ(x)| ≤ [M] · |x − a|ⁿ⁺¹ / (n+1)! = [value]"

  {warn("M is the bound on the (n+1)th derivative, not the nth.")}
  {tip("For eˣ, sin x, cos x: the derivatives are bounded by simple expressions.")}
  {tip("For eˣ on [0, b]: M = eᵇ. Often they'll say 'assume |f⁽ⁿ⁺¹⁾| ≤ M'.")}

{section("FRQ Type: Radius and Interval of Convergence")}

  {BOLD}PERFECT-CREDIT FORMAT:{RESET}

    (1) Apply Ratio Test:
        lim(n→∞) |aₙ₊₁/aₙ| = |x − a| · lim(n→∞) [expression] = L

    (2) Set L < 1:
        |x − a| < R  →  R = [radius of convergence]

    (3) Interval: (a − R, a + R)

    (4) Check endpoints SEPARATELY:
        At x = a − R: Σ [substitute] = [test for convergence]
        At x = a + R: Σ [substitute] = [test for convergence]

    (5) "The interval of convergence is [a−R, a+R) / (a−R, a+R] / [a−R, a+R] / (a−R, a+R)."

  {warn("You MUST check BOTH endpoints. This is worth 1-2 points.")}
  {warn("At endpoints, Ratio Test won't work (L=1). Use other tests (AST, p-series, etc.).")}

{section("FRQ Type: Power Series Manipulation")}

  {BOLD}Common operations:{RESET}

    Differentiation: If f(x) = Σ aₙxⁿ, then f'(x) = Σ naₙxⁿ⁻¹
    Integration: ∫f(x)dx = Σ aₙxⁿ⁺¹/(n+1) + C
    Substitution: Replace x with (−x), (x²), (2x), etc.
    Multiplication: f(x)·g(x) — multiply term by term up to required degree

  {BOLD}"Find the first four nonzero terms of the series for f(x)g(x)."{RESET}
    Multiply term by term, collecting like powers. Only keep up to the degree asked.

  {BOLD}"Find the series for ∫₀ˣ f(t) dt."{RESET}
    Integrate the series term by term. The constant of integration is 0 (lower bound = 0).
"""

# ─────────────────────────────────────────────────────────
# COMMON MULTI-UNIT FRQ TEMPLATES
# ─────────────────────────────────────────────────────────

COMMON_TEMPLATES = f"""
{title("COMMON MULTI-PART FRQ TEMPLATES")}

{section("Template 1: Rate In / Rate Out (Calculator Active)")}
  This appears on almost EVERY exam.

  Setup: R_in(t) = rate flowing in, R_out(t) = rate flowing out, initial amount = A₀.

  {BOLD}(a) Find total amount entering from t = a to t = b.{RESET}
      ∫ₐᵇ R_in(t) dt = [calculator value]   [UNITS]

  {BOLD}(b) Is the amount increasing or decreasing at t = c?{RESET}
      R_in(c) − R_out(c) = [positive or negative]
      "Since R_in(c) − R_out(c) = [value] [> 0 / < 0],
       the amount of [context] is [increasing / decreasing] at t = c."

  {BOLD}(c) Find the amount at time t = b.{RESET}
      A(b) = A₀ + ∫ₐᵇ [R_in(t) − R_out(t)] dt = [value]   [UNITS]

  {BOLD}(d) At what time is the amount at a minimum/maximum?{RESET}
      "R_in(t) = R_out(t) at t = [value]  (set equal, solve on calculator)."
      "R_in − R_out changes from [neg to pos / pos to neg] at t = [value],
       so the amount has a [minimum / maximum] at t = [value]."
      Then evaluate: A(t) = A₀ + ∫₀ᵗ [R_in − R_out] dx = [value]   [UNITS]

{section("Template 2: Table of Values (No Calculator)")}
  Given: table of x, f(x), f'(x), g(x), g'(x) values.

  Common sub-questions:
  • Chain rule: h(x) = f(g(x)) → h'(x) = f'(g(x))·g'(x)
  • Product rule: h(x) = f(x)g(x) → h'(x) = f'(x)g(x) + f(x)g'(x)
  • Quotient rule: h(x) = f(x)/g(x) → h'(x) = [f'g − fg']/g²
  • MVT: "Must there exist c in (a,b) where f'(c) = [f(b)−f(a)]/(b−a)?"
  • Tangent line approximation: L(x) = f(a) + f'(a)(x − a)

  {tip("Show the formula FIRST, then substitute values from the table.")}

{section("Template 3: Graph of f' (No Calculator)")}
  Given: graph of f'(x) (NOT f).

  {BOLD}(a) On what intervals is f increasing?{RESET}
      "f'(x) > 0 on [intervals where graph is above x-axis].
       Therefore f is increasing on those intervals."

  {BOLD}(b) At what x does f have a relative max/min?{RESET}
      "f'(x) changes from positive to negative at x = c.
       Therefore f has a relative maximum at x = c."

  {BOLD}(c) On what intervals is f concave up?{RESET}
      "f'(x) is increasing on [intervals], so f''(x) > 0 on those intervals.
       Therefore f is concave up on those intervals."

  {BOLD}(d) Find f(b) given f(a).{RESET}
      "f(b) = f(a) + ∫ₐᵇ f'(x) dx"
      Compute the integral using geometry (areas under the f' graph).
      "f(b) = [f(a)] + [area] = [value]"

  {warn("Integrals from the graph use GEOMETRIC AREAS (triangles, rectangles, semicircles).")}

{section("Template 4: Particle Motion (Calculator Active)")}
  Given: velocity v(t) or position x(t).

  {BOLD}(a) Is the particle moving left or right at t = c?{RESET}
      "v(c) = [value].  Since v(c) [> 0 / < 0], the particle is moving
       to the [right / left] at t = c."

  {BOLD}(b) Total distance traveled on [a, b].{RESET}
      ∫ₐᵇ |v(t)| dt = [calculator value]   [UNITS: distance units]

  {BOLD}(c) Position at time t = b.{RESET}
      x(b) = x(a) + ∫ₐᵇ v(t) dt = [value]   [UNITS]

  {BOLD}(d) Is speed increasing or decreasing at t = c?{RESET}
      "v(c) = [value], a(c) = v'(c) = [value].
       Since v(c) and a(c) have [same/opposite] signs,
       the speed is [increasing / decreasing] at t = c."

{section("Template 5: Differential Equation (No Calculator)")}
  Given: dy/dx = F(x, y), y(x₀) = y₀.

  {BOLD}(a) Sketch slope field / verify slopes.{RESET}
      "At (x, y) = (1, 2): dy/dx = F(1, 2) = [value].
       The slope segment at (1, 2) has slope [value]."  [repeat for given points]

  {BOLD}(b) Find d²y/dx² and determine concavity.{RESET}
      d²y/dx² = d/dx[F(x,y)]    ← use chain rule: ∂F/∂x + (∂F/∂y)(dy/dx)
      "At (x₀, y₀): d²y/dx² = [value]. Since d²y/dx² [> 0 / < 0], the
       solution curve is concave [up / down] near (x₀, y₀)."

  {BOLD}(c) Find the particular solution by separation of variables.{RESET}
      [See Unit 7 format above]

  {BOLD}(d) Euler's method (BC only).{RESET}
      [See Unit 7 format above]

{section("Template 6: Taylor/Maclaurin Series (No Calculator, BC)")}

  {BOLD}(a) Find the first four nonzero terms and the general term.{RESET}
      Show: f(a), f'(a), f''(a), f'''(a), f⁽⁴⁾(a) ...
      Pₙ(x) = f(a) + f'(a)(x−a) + f''(a)(x−a)²/2! + ...
      General term: f⁽ⁿ⁾(a)(x−a)ⁿ / n!

  {BOLD}(b) Find the radius/interval of convergence.{RESET}
      [See Unit 10 format]

  {BOLD}(c) Use the series to approximate a value or integral.{RESET}
      Substitute x = [value] into the polynomial.
      OR: ∫₀ˣ P(t) dt = [integrate term by term]

  {BOLD}(d) Lagrange error bound.{RESET}
      [See Unit 10 format]
"""

# ─────────────────────────────────────────────────────────
# Menu system
# ─────────────────────────────────────────────────────────

MENU_ITEMS = {
    "0": ("Universal Formatting Rules (READ THIS FIRST)", GLOBAL_RULES),
    "1": ("Unit 1 — Limits & Continuity", UNITS[1]),
    "2": ("Unit 2 — Differentiation: Basics", UNITS[2]),
    "3": ("Unit 3 — Chain, Implicit, Inverse", UNITS[3]),
    "4": ("Unit 4 — Contextual Applications (Related Rates, Motion)", UNITS[4]),
    "5": ("Unit 5 — Analytical Applications (Extrema, MVT)", UNITS[5]),
    "6": ("Unit 6 — Integration & Accumulation", UNITS[6]),
    "7": ("Unit 7 — Differential Equations", UNITS[7]),
    "8": ("Unit 8 — Applications of Integration (Area, Volume)", UNITS[8]),
    "9": ("Unit 9 — Parametric, Polar, Vectors (BC)", UNITS[9]),
    "10": ("Unit 10 — Series (BC)", UNITS[10]),
    "T": ("Common Multi-Part FRQ Templates", COMMON_TEMPLATES),
    "A": ("Show ALL (full reference dump)", None),
    "Q": ("Quit", None),
}


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def show_menu():
    print(title("AP CALCULUS BC — FRQ PERFECT-CREDIT REFERENCE"))
    print(f"  {BOLD}Select a section:{RESET}\n")
    for key, (label, _) in MENU_ITEMS.items():
        pad = " " if len(key) == 1 else ""
        print(f"    {CYAN}{BOLD}[{key}]{RESET} {pad}{label}")
    print()


def paginate(text):
    """Print text, paging if terminal is available."""
    lines = text.split("\n")
    try:
        rows = os.get_terminal_size().lines - 2
    except OSError:
        rows = 40
    for i in range(0, len(lines), rows):
        print("\n".join(lines[i : i + rows]))
        if i + rows < len(lines):
            try:
                inp = input(f"\n{DIM}— Press Enter for more, 'q' to return to menu —{RESET} ")
                if inp.strip().lower() == "q":
                    return
            except EOFError:
                return


def main():
    clear()
    while True:
        show_menu()
        try:
            choice = input(f"  {BOLD}Enter choice: {RESET}").strip().upper()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if choice == "Q":
            print("\nGoodbye — go get that 5!")
            break
        elif choice == "A":
            clear()
            all_text = GLOBAL_RULES
            for i in range(1, 11):
                all_text += UNITS[i]
            all_text += COMMON_TEMPLATES
            paginate(all_text)
            input(f"\n{DIM}— Press Enter to return to menu —{RESET} ")
            clear()
        elif choice in MENU_ITEMS:
            clear()
            paginate(MENU_ITEMS[choice][1])
            input(f"\n{DIM}— Press Enter to return to menu —{RESET} ")
            clear()
        else:
            print(f"\n  {RED}Invalid choice. Try again.{RESET}\n")


if __name__ == "__main__":
    main()
