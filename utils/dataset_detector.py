SALES_COLUMNS = {
    "sales",
    "revenue",
    "profit",
    "customer",
    "product",
    "order",
    "quantity",
    "discount",
    "city"
}

EMPLOYEE_COLUMNS = {
    "employee",
    "salary",
    "department",
    "designation",
    "joining",
    "gender",
    "manager"
}

LOGISTICS_COLUMNS = {
    "shipment",
    "warehouse",
    "route",
    "driver",
    "delivery",
    "vehicle",
    "dispatch"
}

def detect_dataset_type(df):
    """
    Detects dataset type based on column names.
    """
    columns = [column.lower().strip() for column in df.columns]
    sales_score = 0
    employee_score = 0
    logistics_score = 0
    for column in columns:
      for keyword in SALES_COLUMNS:
        if keyword in column:
            sales_score += 1
      for keyword in EMPLOYEE_COLUMNS:
        if keyword in column:
            employee_score += 1
      for keyword in LOGISTICS_COLUMNS:
        if keyword in column:
            logistics_score += 1

    scores = {
    "Sales Dataset": sales_score,
    "Employee Dataset": employee_score,
    "Logistics Dataset": logistics_score
}

    highest_score = max(scores.values())

    if highest_score == 0:
     return "Generic Dataset"

    dataset_type = max(scores, key=scores.get)

    return dataset_type