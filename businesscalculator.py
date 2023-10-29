from datetime import datetime

class BusinessMetricsCalculator:
    def __init__(self, coefficients):
        """
        Initialize the BusinessMetricsCalculator with the regression coefficients.

        :param coefficients: Dictionary containing the coefficients from the regression model.
        """
        if not isinstance(coefficients, dict):
            raise ValueError("Coefficients must be provided as a dictionary.")
        self.coefficients = coefficients

    def calculate_roi(self, investment_variable, investment_amount):
        """
        Calculates the Return on Investment (ROI) for the specified investment variable.

        :param investment_variable: Name of the investment variable in the regression model.
        :param investment_amount: Specific amount of investment.
        :return: ROI as a percentage.
        """
        try:
            coefficient = self.coefficients[investment_variable]
        except KeyError:
            raise ValueError(f"{investment_variable} not found in coefficients dictionary.")
        
        if investment_amount == 0:
            raise ValueError("Investment amount cannot be zero.")
        
        predicted_increase = coefficient * investment_amount
        roi = (predicted_increase / investment_amount) * 100
        return roi

    def calculate_margin(self, revenue, cost):
        """
        Calculates the margin as a percentage of revenue.

        :param revenue: Total revenue.
        :param cost: Total cost.
        :return: Margin as a percentage.
        """
        if revenue == 0:
            raise ValueError("Revenue cannot be zero.")
        
        margin = (revenue - cost) / revenue * 100
        return margin

    def calculate_elasticity(self, price_coefficient):
        """
        Calculates the elasticity of demand based on the price coefficient.

        :param price_coefficient: Coefficient for the price variable in the regression model.
        :return: Elasticity of demand.
        """
        if not isinstance(price_coefficient, (int, float)):
            raise ValueError("Price coefficient must be a number.")
        
        elasticity = abs(price_coefficient)
        return elasticity

    def calculate_growth_rate(self, previous_value, current_value):
        """
        Calculates the growth rate between two periods.

        :param previous_value: Value in the previous period.
        :param current_value: Value in the current period.
        :return: Growth rate as a percentage.
        """
        if previous_value == 0:
            raise ValueError("Previous value cannot be zero.")
        
        growth_rate = ((current_value - previous_value) / previous_value) * 100
        return growth_rate

    def calculate_breakeven_point(self, fixed_costs, variable_cost_per_unit, selling_price_per_unit):
        """
        Calculates the breakeven point in units sold.

        :param fixed_costs: Total fixed costs.
        :param variable_cost_per_unit: Variable cost per unit.
        :param selling_price_per_unit: Selling price per unit.
        :return: Breakeven point in units.
        """
        if selling_price_per_unit <= variable_cost_per_unit:
            raise ValueError("Selling price per unit must be greater than variable cost per unit.")
        
        breakeven_point = fixed_costs / (selling_price_per_unit - variable_cost_per_unit)
        return breakeven_point

    def calculate_cltv(self, average_purchase_value, purchase_frequency, customer_lifetime, profit_margin):
        """
        Calculates the Customer Lifetime Value (CLTV).

        :param average_purchase_value: Average purchase value.
        :param purchase_frequency: Purchase frequency per period.
        :param customer_lifetime: Expected customer lifetime in periods.
        :param profit_margin: Profit margin as a percentage.
        :return: CLTV.
        """
        if profit_margin < 0 or profit_margin > 100:
            raise ValueError("Profit margin must be between 0 and 100.")
        
        cltv = (average_purchase_value * purchase_frequency * customer_lifetime) * (profit_margin / 100)
        return cltv

    def calculate_inventory_turnover(self, cost_of_goods_sold, average_inventory_value):
        """
        Calculates the Inventory Turnover Ratio.

        :param cost_of_goods_sold: Cost of goods sold in a period.
        :param average_inventory_value: Average inventory value for the period.
        :return: Inventory Turnover Ratio.
        """
        if average_inventory_value == 0:
            raise ValueError("Average inventory value cannot be zero.")
        
        inventory_turnover = cost_of_goods_sold / average_inventory_value
        return inventory_turnover

    def calculate_cagr(self, initial_value, final_value, number_of_periods):
        """
        Calculates the Compound Annual Growth Rate (CAGR).

        :param initial_value: Initial value.
        :param final_value: Final value.
        :param number_of_periods: Number of periods over which growth occurred.
        :return: CAGR as a percentage.
        """
        if initial_value == 0:
            raise ValueError("Initial value cannot be zero.")
        if number_of_periods == 0:
            raise ValueError("Number of periods cannot be zero.")
        
        cagr = ((final_value / initial_value) ** (1 / number_of_periods) - 1) * 100
        return cagr

    def calculate_npv(self, cash_flows, discount_rate):
        """
        Calculates the Net Present Value (NPV) of a series of cash flows.

        :param cash_flows: List of cash flows, including initial investment (negative) and subsequent inflows.
        :param discount_rate: Discount rate as a percentage.
        :return: NPV.
        """
        if not isinstance(cash_flows, list) or len(cash_flows) == 0:
            raise ValueError("Cash flows must be a non-empty list.")
        if discount_rate < 0 or discount_rate > 100:
            raise ValueError("Discount rate must be between 0 and 100.")
        
        npv = sum(cf / (1 + discount_rate / 100) ** i for i, cf in enumerate(cash_flows))
        return npv

    def calculate_conversion_rate(self, number_of_conversions, total_visitors):
        """
        Calculates the conversion rate.

        :param number_of_conversions: Number of successful conversions (e.g., purchases).
        :param total_visitors: Total number of visitors or users.
        :return: Conversion rate as a percentage.
        """
        if total_visitors == 0:
            raise ValueError("Total visitors cannot be zero.")
        
        conversion_rate = (number_of_conversions / total_visitors) * 100
        return conversion_rate

    def calculate_payback_period(self, initial_investment, cash_inflows):
        """
        Calculates the Payback Period.

        :param initial_investment: Initial investment amount.
        :param cash_inflows: List of cash inflows per period.
        :return: Payback period in periods.
        """
        if not isinstance(cash_inflows, list) or len(cash_inflows) == 0:
            raise ValueError("Cash inflows must be a non-empty list.")
        
        cumulative_cash_inflows = 0
        for period, inflow in enumerate(cash_inflows, 1):
            cumulative_cash_inflows += inflow
            if cumulative_cash_inflows >= initial_investment:
                return period

    def calculate_operating_leverage(self, contribution_margin, net_operating_income):
        """
        Calculates the Operating Leverage.

        :param contribution_margin: Contribution margin for the period.
        :param net_operating_income: Net operating income for the period.
        :return: Operating leverage.
        """
        if net_operating_income == 0:
            raise ValueError("Net operating income cannot be zero.")
        
        return contribution_margin / net_operating_income

    def calculate_quick_ratio(self, cash, accounts_receivable, current_liabilities):
        """
        Calculates the Quick Ratio.

        :param cash: Cash and cash equivalents.
        :param accounts_receivable: Accounts receivable.
        :param current_liabilities: Current liabilities.
        :return: Quick ratio.
        """
        if current_liabilities == 0:
            raise ValueError("Current liabilities cannot be zero.")
        
        return (cash + accounts_receivable) / current_liabilities

    def calculate_roa(self, net_income, total_assets):
        """
        Calculates the Return on Assets (ROA).

        :param net_income: Net income for the period.
        :param total_assets: Total assets.
        :return: ROA as a percentage.
        """
        if total_assets == 0:
            raise ValueError("Total assets cannot be zero.")
        
        return (net_income / total_assets) * 100

    def calculate_churn_rate(self, number_of_churned_customers, total_customers_at_start):
        """
        Calculates the Churn Rate.

        :param number_of_churned_customers: Number of customers who churned during the period.
        :param total_customers_at_start: Total number of customers at the start of the period.
        :return: Churn rate as a percentage.
        """
        if total_customers_at_start == 0:
            raise ValueError("Total customers at start cannot be zero.")
        
        return (number_of_churned_customers / total_customers_at_start) * 100

    def calculate_roe(self, net_income, shareholders_equity):
        """
        Calculates the Return on Equity (ROE).

        :param net_income: Net income for the period.
        :param shareholders_equity: Shareholders' equity.
        :return: ROE as a percentage.
        """
        if shareholders_equity == 0:
            raise ValueError("Shareholders' equity cannot be zero.")
        
        return (net_income / shareholders_equity) * 100

    def calculate_current_ratio(self, current_assets, current_liabilities):
        """
        Calculates the Current Ratio.

        :param current_assets: Current assets.
        :param current_liabilities: Current liabilities.
        :return: Current ratio.
        """
        if current_liabilities == 0:
            raise ValueError("Current liabilities cannot be zero.")
        
        return current_assets / current_liabilities

    def calculate_cac(self, marketing_expenses, number_of_new_customers):
        """
        Calculates the Customer Acquisition Cost (CAC).

        :param marketing_expenses: Total marketing expenses.
        :param number_of_new_customers: Number of new customers acquired.
        :return: CAC.
        """
        if number_of_new_customers == 0:
            raise ValueError("Number of new customers cannot be zero.")
        
        return marketing_expenses / number_of_new_customers

    def calculate_customer_retention_rate(self, number_of_customers_at_end, number_of_new_customers, total_customers_at_start):
        """
        Calculates the Customer Retention Rate.

        :param number_of_customers_at_end: Number of customers at the end of the period.
        :param number_of_new_customers: Number of new customers acquired during the period.
        :param total_customers_at_start: Total number of customers at the start of the period.
        :return: Customer retention rate as a percentage.
        """
        if total_customers_at_start == 0:
            raise ValueError("Total customers at start cannot be zero.")
        
        number_of_customers_retained = number_of_customers_at_end - number_of_new_customers
        return (number_of_customers_retained / total_customers_at_start) * 100

    def calculate_gross_profit_margin(self, gross_profit, revenue):
        """
        Calculates the Gross Profit Margin.

        :param gross_profit: Gross profit.
        :param revenue: Total revenue.
        :return: Gross profit margin as a percentage.
        """
        if revenue == 0:
            raise ValueError("Revenue cannot be zero.")
        
        return (gross_profit / revenue) * 100

    def calculate_ebit(self, revenue, operating_expenses):
        """
        Calculates Earnings Before Interest and Taxes (EBIT).

        :param revenue: Total revenue.
        :param operating_expenses: Total operating expenses.
        :return: EBIT.
        """
        return revenue - operating_expenses

    def calculate_eps(self, net_income, number_of_shares):
        """
        Calculates Earnings Per Share (EPS).

        :param net_income: Net income for the period.
        :param number_of_shares: Total number of shares.
        :return: EPS.
        """
        if number_of_shares == 0:
            raise ValueError("Number of shares cannot be zero.")
        
        return net_income / number_of_shares

    def calculate_pe_ratio(self, market_price_per_share, earnings_per_share):
        """
        Calculates Price to Earnings (P/E) Ratio.

        :param market_price_per_share: Market price per share.
        :param earnings_per_share: Earnings per share.
        :return: P/E ratio.
        """
        if earnings_per_share == 0:
            raise ValueError("Earnings per share cannot be zero.")
        
        return market_price_per_share / earnings_per_share

    def calculate_debt_to_equity(self, total_debt, shareholders_equity):
        """
        Calculates Debt to Equity Ratio.

        :param total_debt: Total debt.
        :param shareholders_equity: Shareholders' equity.
        :return: Debt to equity ratio.
        """
        if shareholders_equity == 0:
            raise ValueError("Shareholders' equity cannot be zero.")
        
        return total_debt / shareholders_equity

    def calculate_working_capital(self, current_assets, current_liabilities):
        """
        Calculates Working Capital.

        :param current_assets: Current assets.
        :param current_liabilities: Current liabilities.
        :return: Working capital.
        """
        return current_assets - current_liabilities

    def calculate_ltv_cac_ratio(self, lifetime_value, customer_acquisition_cost):
        """
        Calculates Lifetime Value to Customer Acquisition Cost (LTV/CAC) Ratio.

        :param lifetime_value: Customer lifetime value.
        :param customer_acquisition_cost: Customer acquisition cost.
        :return: LTV/CAC ratio.
        """
        if customer_acquisition_cost == 0:
            raise ValueError("Customer acquisition cost cannot be zero.")
        
        return lifetime_value / customer_acquisition_cost

    def calculate_aov(self, total_revenue, number_of_orders):
        """
        Calculates Average Order Value (AOV).

        :param total_revenue: Total revenue from orders.
        :param number_of_orders: Total number of orders.
        :return: AOV.
        """
        if number_of_orders == 0:
            raise ValueError("Number of orders cannot be zero.")
        
        return total_revenue / number_of_orders

    def analyze_nps(self, promoters, passives, detractors):
        """
        Analyzes Net Promoter Score (NPS).

        :param promoters: Number of promoters.
        :param passives: Number of passives.
        :param detractors: Number of detractors.
        :return: NPS as a percentage.
        """
        total_respondents = promoters + passives + detractors
        if total_respondents == 0:
            raise ValueError("Total number of respondents cannot be zero.")
        
        return (promoters - detractors) / total_respondents * 100

    def calculate_lead_conversion_rate(self, number_of_leads_converted, total_leads):
        """
        Calculates Lead Conversion Rate.

        :param number_of_leads_converted: Number of leads converted.
        :param total_leads: Total number of leads.
        :return: Lead conversion rate as a percentage.
        """
        if total_leads == 0:
            raise ValueError("Total number of leads cannot be zero.")
        
        return (number_of_leads_converted / total_leads) * 100

    def calculate_cpl(self, marketing_expenses, total_leads):
        """
        Calculates Cost Per Lead (CPL).

        :param marketing_expenses: Total marketing expenses.
        :param total_leads: Total number of leads.
        :return: CPL.
        """
        if total_leads == 0:
            raise ValueError("Total number of leads cannot be zero.")
        
        return marketing_expenses / total_leads

    def calculate_time_to_market(self, start_date, launch_date):
        """
        Calculates Time to Market for New Products.

        :param start_date: Start date of the project (string, format: 'YYYY-MM-DD').
        :param launch_date: Launch date of the product (string, format: 'YYYY-MM-DD').
        :return: Time to market in days.
        """
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            launch_date = datetime.strptime(launch_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")
        
        return (launch_date - start_date).days

    def calculate_employee_turnover_rate(self, number_of_leavers, average_number_of_employees):
        """
        Calculates Employee Turnover Rate.

        :param number_of_leavers: Number of employees who left during the period.
        :param average_number_of_employees: Average number of employees during the period.
        :return: Employee turnover rate as a percentage.
        """
        if average_number_of_employees == 0:
            raise ValueError("Average number of employees cannot be zero.")
        
        return (number_of_leavers / average_number_of_employees) * 100

    def measure_employee_productivity(self, total_output, total_input):
        """
        Measures Employee Productivity.

        :param total_output: Total output produced.
        :param total_input: Total input (e.g., hours worked).
        :return: Employee productivity ratio.
        """
        if total_input == 0:
            raise ValueError("Total input cannot be zero.")
        
        return total_output / total_input

if __name__ == "__main__":
    # Your coefficients
    coefficients = {
        'investment_variable': 0.1,
        'price': -0.05,
        # Add other coefficients as needed
    }
    
    # Instantiate the calculator
    calculator = BusinessMetricsCalculator(coefficients)

    # Hardcoded test values
    investment_value = 1000
    revenue = 1000
    cost = 800
    growth_start = 100
    growth_end = 110
    fixed_cost = 1000
    variable_cost = 10
    selling_price = 50
    average_order_value = 100
    purchase_frequency = 2
    customer_lifespan = 5
    discount_rate = 20
    inventory_cost = 5000
    average_inventory = 1000
    initial_value = 100
    final_value = 200
    time_period = 5
    cash_flows = [100, 200, 300]
    total_visitors = 1000
    total_conversions = 100
    initial_investment = 1000
    payback_cash_flows = [200, 300, 500]
    fixed_costs = 1000
    variable_costs = 200
    current_assets = 100
    current_liabilities = 50
    inventory_value = 150
    net_income = 1000
    total_assets = 5000
    churned_customers = 50
    total_customers = 500
    net_profit = 1000
    total_equity = 5000
    accounts_receivable = 1000
    accounts_payable = 500
    customer_lifetime_value = 1000
    customer_acquisition_cost = 100
    total_orders = 10
    promoters = 100
    passives = 50
    detractors = 50
    total_leads = 1000
    total_lead_conversion = 100
    total_marketing_spend = 1000
    total_leads_generated = 100
    start_date = '2022-01-01'
    end_date = '2022-01-30'
    total_employees = 100
    employees_left = 10
    total_revenue = 1000
    total_employees_for_productivity = 100

    # Calculate and print results for all functions
    print(f"ROI: {calculator.calculate_roi('investment_variable', investment_value)}%")
    print(f"Margin: {calculator.calculate_margin(revenue, cost)}%")
    print(f"Elasticity: {calculator.calculate_elasticity(coefficients['price'])}")
    print(f"Growth Rate: {calculator.calculate_growth_rate(growth_start, growth_end)}%")
    print(f"Breakeven Point: {calculator.calculate_breakeven_point(fixed_cost, variable_cost, selling_price)} units")
    print(f"CLTV: {calculator.calculate_cltv(average_order_value, purchase_frequency, customer_lifespan, discount_rate)}")
    print(f"Inventory Turnover: {calculator.calculate_inventory_turnover(inventory_cost, average_inventory)}")
    print(f"CAGR: {calculator.calculate_cagr(initial_value, final_value, time_period)}%")
    print(f"NPV: {calculator.calculate_npv(cash_flows, discount_rate)}")
    print(f"Conversion Rate: {calculator.calculate_conversion_rate(total_conversions, total_visitors)}%")
    print(f"Payback Period: {calculator.calculate_payback_period(initial_investment, payback_cash_flows)} periods")
    print(f"Operating Leverage: {calculator.calculate_operating_leverage(fixed_costs, variable_costs)}")
    print(f"Quick Ratio: {calculator.calculate_quick_ratio(current_assets, current_liabilities, inventory_value)}")
    print(f"ROA: {calculator.calculate_roa(net_income, total_assets)}%")
    print(f"Churn Rate: {calculator.calculate_churn_rate(churned_customers, total_customers)}%")
    print(f"ROE: {calculator.calculate_roe(net_profit, total_equity)}%")
    print(f"Current Ratio: {calculator.calculate_current_ratio(accounts_receivable, accounts_payable)}")
    print(f"CAC: {calculator.calculate_cac(total_marketing_spend, total_leads_generated)}")
    print(f"Customer Retention Rate: {calculator.calculate_customer_retention_rate(total_customers, churned_customers, total_customers)}%")
    print(f"Gross Profit Margin: {calculator.calculate_gross_profit_margin(revenue, cost)}%")
    print(f"EBIT: {calculator.calculate_ebit(revenue, cost)}")
    print(f"EPS: {calculator.calculate_eps(net_income, total_orders)}")
    print(f"P/E Ratio: {calculator.calculate_pe_ratio(selling_price, net_income)}")
    print(f"Debt to Equity: {calculator.calculate_debt_to_equity(current_liabilities, total_equity)}")
    print(f"Working Capital: {calculator.calculate_working_capital(current_assets, current_liabilities)}")
    print(f"LTV/CAC Ratio: {calculator.calculate_ltv_cac_ratio(customer_lifetime_value, customer_acquisition_cost)}")
    print(f"AOV: {calculator.calculate_aov(revenue, total_orders)}")
    print(f"NPS: {calculator.analyze_nps(promoters, passives, detractors)}%")
    print(f"Lead Conversion Rate: {calculator.calculate_lead_conversion_rate(total_lead_conversion, total_leads)}%")
    print(f"CPL: {calculator.calculate_cpl(total_marketing_spend, total_leads_generated)}")
    print(f"Time to Market: {calculator.calculate_time_to_market(start_date, end_date)} days")
    print(f"Employee Turnover Rate: {calculator.calculate_employee_turnover_rate(employees_left, total_employees)}%")
    print(f"Employee Productivity: {calculator.measure_employee_productivity(total_revenue, total_employees_for_productivity)}")