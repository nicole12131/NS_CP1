# NS 1st 💡Crew Shares 

total_earned = float(input("How much was earned: "))
num_crew = int(input("How many crew members are there (not including the captain and first mate): "))

captain_shares = 7
first_mate_shares = 3
crew_shares = num_crew

total_shares = captain_shares + first_mate_shares + crew_shares

advance_paid = num_crew * 500
remaining_treasure = total_earned - advance_paid

share_value = remaining_treasure / total_shares

captain_gets = captain_shares * share_value
first_mate_gets = first_mate_shares * share_value
crew_still_needs = share_value - 500 if share_value > 500 else 0

print(f"\nHow much was earned: {total_earned:.2f}")
print(f"How many crew members are there (not including the captain and first mate): {num_crew}")
print(f"\nThe captain gets: ${captain_gets:.2f}")
print(f"The first mate gets: ${first_mate_gets:.2f}")
print(f"Crew still needs: ${crew_still_needs:.2f}")