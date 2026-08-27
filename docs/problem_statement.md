# Problem Statement: Lychee — Multi-Venue Restaurant Inventory Tracker

## The Problem

Restaurants split inventory across three categories that behave very differently from each other. Bar stock (spirits, wine, mixers) is usually counted by partial bottle. Dry goods (shelf-stable staples) are usually counted by case or unit. Cold goods (perishables) are counted by weight or count, turn over faster, and carry a higher cost of error since spoiled stock cannot be sold at all. Most inventory tools treat all of these as generic line items with a quantity, which does not match how kitchen and bar staff actually think about what is on the shelf.

The problem compounds for restaurant groups where two venues share one physical kitchen. This is a common industry setup: a single walk-in cooler, dry storage room, and bar back stock physically hold ingredients for two separate concepts, such as a daytime cafe and an evening bar service operating out of the same space. Each venue still needs its own accurate inventory picture for costing, ordering, and waste tracking, even though the physical stock is shared. Staff need a way to draw down or move stock between the two venues without duplicating counts or losing track of which venue is responsible for what.

The people doing the actual counting are usually rotating hourly staff, not managers, and are not necessarily comfortable with software. They need to log counts quickly, often mid-shift, using the informal measurements they already think in, such as two-thirds of a bottle, one case, or three heads of lettuce, rather than being forced to convert everything into a standardized unit before they can record anything. When entry is slow or confusing, counts get skipped, and the data stops being trustworthy.

Because counts happen throughout the day on whatever device is closest, a phone at the bar, a tablet in the kitchen, a laptop in the office, the numbers need to stay consistent across all of them in close to real time. A count logged at the bar should be reflected in a manager's cost report within seconds, not after an overnight batch sync.

## Target Users

- **Primary users:** rotating front- and back-of-house staff who record inventory counts during or between shifts. They need speed and simple, forgiving input over precision or configuration.
- **Secondary users:** shift leads, kitchen managers, and owners who review stock levels, transfer inventory between venues, place orders, and reconcile costs.

## Core Pain Points

1. Inventory spans bar, dry, and cold categories, each with different natural units and different tolerance for delay between count and action.
2. Two venues can draw from one shared physical stockroom, so inventory needs to be tracked at both the shared-pool level and the per-venue level, with transfers recorded between them.
3. Data entry is done quickly by non-technical, rotating staff using informal, often fractional measurements rather than standardized units.
4. Counts need to happen often enough that shrinkage, waste, and low-stock situations are caught before they become a problem, not discovered days later.
5. Different roles use different devices at different times, so the system has to keep everyone looking at current, matching numbers.

## Proposed Solution

Lychee intends to solve this by giving restaurant staff a fast, forgiving way to log stock counts in the units they already use, rather than asking them to convert to a standardized unit before they can record anything. Lychee intends to treat bar, dry, and cold goods as distinct categories, each with its own natural units and its own expected update cadence, instead of flattening every item into a generic line with a quantity.

For venues that share one physical kitchen, Lychee intends to track inventory at both the shared-pool and per-venue level, so stock can be drawn down or transferred between venues without duplicating counts or losing track of ownership. And because counts come from different people on different devices throughout the day, Lychee intends to keep everyone, whether they are on a phone at the bar or a laptop in the office, looking at the same close-to-real-time numbers.

Solved well, this closes the gap between inventory data that reflects what is actually on the shelf and inventory data that everyone quietly stops trusting.
