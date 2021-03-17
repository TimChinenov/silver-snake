import silver_meal as sm

if __name__ == "__main__":
    demand = [18, 30, 42, 5, 20]
    production_cost = 80.0
    holding_cost = 2.0

    lot_planner = sm.SilverMeal()
    lot_planner.set_demands_for_intervals(demand)
    lot_planner.set_cost_per_production(production_cost)
    lot_planner.set_holding_cost(holding_cost)

    (lot_plan, lot_cost) = lot_planner.compute_lot_production()

    print(lot_plan)
    print(lot_cost)
    print(sum(lot_cost))

    demand = [12, 42, 1 , 200, 1, 90, 1, 1000, 2, 4, 21, 34]
    production_cost = 30.0
    holding_cost = 1.2

    lot_planner = sm.SilverMeal()
    lot_planner.set_demands_for_intervals(demand)
    lot_planner.set_cost_per_production(production_cost)
    lot_planner.set_holding_cost(holding_cost)

    (lot_plan, lot_cost) = lot_planner.compute_lot_production()

    print(lot_plan)
    print(lot_cost)
    print(sum(lot_cost))
