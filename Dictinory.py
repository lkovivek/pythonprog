financials={
    "Q1":{"revenue":50,"expense":10},
    "Q2":{"revenue":60,"expense":30},
    "Q3":{"revenue":55,"expense":35},
    "Q4":{"revenue":-10,"expense":35},
}

for quarter,data in financials.items():
    if data["revenue"]<0:
        print(f"Invalid revenue for {quarter}. skipping.")
        continue
    margin=(data["revenue"]-data["expense"])/data["revenue"]*100
    print(f"In {quarter}: {margin:.2f}%")