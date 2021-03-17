class SilverMeal:
    def __init__(self):
        self.demands_for_intervals = []
        self.cost_per_production = 0
        self.holding_cost = 0
    
    def set_demands_for_intervals(self, demands_for_intervals):
        self.demands_for_intervals = demands_for_intervals

    def set_cost_per_production(self, cost_per_production):
        self.cost_per_production = cost_per_production

    def set_holding_cost(self, holding_cost):
        self.holding_cost = holding_cost

    def compute_lot_production(self):
        previous_cost = self.cost_per_production * 1.0
        end_of_last_interval = 0
        current_interval = 1
        interval = 1
        lot_plan = []
        lot_plan_avg_costs = []
        lot_plan_costs = []

        for demand in self.demands_for_intervals[1:]:

            interval_cost = ((previous_cost * interval) + (interval) * self.holding_cost * demand) / (interval + 1)

            if interval_cost > previous_cost:
                lot_plan_avg_costs.append(previous_cost)
                lot_plan_costs.append(previous_cost * interval)
                lot_plan.append(self.demands_for_intervals[end_of_last_interval: current_interval])
                end_of_last_interval = current_interval
                interval = 1
                previous_cost = self.cost_per_production
            else:
                previous_cost = interval_cost
                interval += 1

            current_interval += 1 

        if end_of_last_interval != current_interval:
            lot_plan.append(self.demands_for_intervals[end_of_last_interval:])
            lot_plan_costs.append(previous_cost * interval)
            lot_plan_avg_costs.append(previous_cost)

        return (lot_plan, lot_plan_costs)

