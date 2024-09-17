# Install the necessary libraries
#!pip install streamlit plotly

import streamlit as st
import plotly.express as px
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap

# Define the hex colors, including light gray for nonexistent hunting opportunities
hex_colors_with_light_gray = ['#d3d3d3', '#f3e4c7', '#d8c9ac', '#a09984', '#868374', '#6e6e60', '#575a50', '#3f4741', '#26302f', '#071114']

# Create a custom colormap with the specified colors
cmap = LinearSegmentedColormap.from_list("custom_cmap", hex_colors_with_light_gray, N=256)

deer_hunting_data = {
    'State': ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'],
    'Score': [8, 4, 5, 7, 3, 9, 6, 5, 4, 8, 2, 9, 8, 7, 9, 10, 9, 6, 5, 6, 5, 8, 9, 8, 9, 9, 8, 3, 6, 5, 5, 7, 7, 8, 9, 8, 6, 8, 4, 7, 9, 8, 10, 7, 6, 7, 5, 8, 10, 9],
    'Description': [
        'Alabama offers a large population of whitetail deer with plenty of public land. However, hunting pressure is high.',
        'Alaska has unique hunting experiences, but limited deer population and difficult terrain make it challenging.',
        'Arizona’s deer hunting is known for its beautiful scenery, but public land access can be limited.',
        'Arkansas offers good hunting on both public and private lands, though hunting pressure can be moderate.',
        'California has diverse landscapes, but strict regulations and limited public hunting land can be a con.',
        'Colorado boasts high-quality hunting with lots of public land. However, competition can be intense.',
        'Connecticut offers decent hunting, but public land is scarce and hunting regulations are strict.',
        'Delaware has manageable deer populations, but limited public land options for hunters.',
        'Florida’s deer are smaller, and hunting can be difficult in dense vegetation. Public land is limited.',
        'Georgia has a high deer population and plenty of public land, but hunting pressure is significant.',
        'Hawaii offers a unique hunting experience, but deer populations are lower and hunting is less popular.',
        'Idaho has excellent hunting on public lands with various terrains, but some areas can be remote.',
        'Illinois is known for trophy bucks, but hunting is largely on private land, requiring permits or leases.',
        'Indiana provides a balanced hunting experience with decent public land and moderate deer populations.',
        'Iowa is famous for its trophy whitetails, but hunting is primarily on private land with limited public access.',
        'Kansas has some of the best deer hunting in the country with large deer populations and less hunting pressure.',
        'Kentucky offers high-quality hunting with plenty of public land and a healthy deer population.',
        'Louisiana has decent deer populations, but hunting pressure and limited public land can be challenging.',
        'Maine offers a rugged hunting experience, but deer densities are lower, especially in the northern regions.',
        'Maryland has good hunting opportunities, though public land is somewhat limited and hunting pressure is moderate.',
        'Massachusetts provides decent deer hunting, but public land is limited and hunting regulations are strict.',
        'Michigan has a high deer population and abundant public land, but hunting pressure can be very high.',
        'Minnesota offers vast public lands and great deer hunting, though winters can be harsh for hunters.',
        'Mississippi boasts a strong deer population and plenty of public land, but hunting pressure is high.',
        'Missouri has excellent hunting with a mix of public and private lands, and manageable hunting pressure.',
        'Montana offers vast, scenic public lands with diverse hunting opportunities, but some areas are remote.',
        'Nebraska provides solid deer hunting with access to public lands, but hunting pressure is variable.',
        'Nevada has limited deer hunting opportunities due to its desert terrain and lower deer populations.',
        'New Hampshire offers a challenging hunt in forested terrain, but deer populations are lower.',
        'New Jersey has a decent deer population but limited public land and heavy regulations.',
        'New Mexico has beautiful landscapes, but deer populations are lower and public land can be remote.',
        'New York provides a variety of hunting environments with good deer populations, but hunting pressure is high.',
        'North Carolina has good public hunting lands and a healthy deer population, though pressure is moderate.',
        'North Dakota offers great hunting with less pressure and abundant public land, though winters can be severe.',
        'Ohio is known for its trophy deer and good public hunting lands, but hunting pressure can be intense.',
        'Oklahoma has a mix of private and public land hunting with solid deer populations.',
        'Oregon offers diverse hunting environments, but deer populations can be lower in some areas.',
        'Pennsylvania has a large deer population and abundant public land, though hunting pressure is high.',
        'Rhode Island has limited public hunting land, though deer populations are relatively healthy.',
        'South Carolina provides good deer hunting with varied terrain, though public land access is limited.',
        'South Dakota offers great hunting opportunities with abundant public land and less pressure.',
        'Tennessee has a good deer population with various public lands, though hunting pressure can be moderate.',
        'Texas is renowned for its exceptional deer hunting, with large ranches and diverse environments.',
        'Utah offers great public land hunting in beautiful settings, though deer densities can be variable.',
        'Vermont provides a classic hunting experience in dense forests, but deer populations are lower.',
        'Virginia has solid public hunting lands and a healthy deer population, with moderate hunting pressure.',
        'Washington offers varied hunting terrains, though deer populations and public access can be limited.',
        'West Virginia has abundant deer and public land, offering a quality hunting experience.',
        'Wisconsin is known for its trophy deer and diverse hunting environments, though hunting pressure is high.',
        'Wyoming offers fantastic hunting in scenic areas with diverse terrain, but some areas are remote.'
    ]
}

duck_hunting_data = {
    'State': ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'],
    'Score': [8, 9, 5, 10, 8, 7, 6, 8, 7, 7, 4, 7, 9, 6, 7, 8, 6, 10, 4, 9, 6, 8, 9, 9, 9, 7, 8, 5, 5, 6, 6, 7, 9, 7, 8, 8, 7, 5, 5, 7, 8, 9, 10, 8, 5, 7, 9, 4, 10, 8],
    'Description': [
        'Alabama offers great duck hunting with a variety of waterfowl and many public hunting areas.',
        'Alaska provides a unique duck hunting experience, with vast wetlands and diverse species.',
        'Arizona has limited waterfowl hunting, but certain wetlands attract migratory ducks during the season.',
        'Arkansas is one of the top duck hunting states, with flooded timber and abundant waterfowl in the Mississippi Flyway.',
        'California has diverse wetlands and public hunting areas, but hunting pressure can be high.',
        'Colorado offers decent duck hunting, especially in the eastern plains and along the South Platte River.',
        'Connecticut has moderate waterfowl hunting with a mix of coastal and inland wetlands.',
        'Delaware’s location along the Atlantic Flyway makes it a great spot for duck hunting, with numerous marshes and bays.',
        'Florida provides a unique hunting experience with a mix of species, particularly in its coastal marshes and lakes.',
        'Georgia has good duck hunting, particularly in its coastal areas and along the Savannah River.',
        'Hawaii offers limited duck hunting opportunities, mostly focused on local species in specific wetlands.',
        'Idaho has a variety of duck hunting environments, particularly in its northern lakes and river systems.',
        'Illinois is known for its waterfowl hunting along the Mississippi River and central state marshlands.',
        'Indiana provides decent duck hunting, with opportunities in marshes, rivers, and reservoirs across the state.',
        'Iowa offers solid hunting opportunities, particularly along the Mississippi and Missouri Rivers.',
        'Kansas has diverse wetlands and public lands, offering good hunting during the migration season.',
        'Kentucky provides decent duck hunting, with opportunities along rivers and in managed wetlands.',
        'Louisiana is a top destination for duck hunters, known for its coastal marshes and the Mississippi Flyway.',
        'Maine has a limited season, but offers hunting in its coastal regions and northern lakes.',
        'Maryland is famous for Chesapeake Bay, providing world-class duck hunting opportunities.',
        'Massachusetts offers coastal and inland duck hunting, though public land access can be limited.',
        'Michigan has excellent duck hunting, particularly in its Great Lakes coastal marshes and inland lakes.',
        'Minnesota is a prime waterfowl state, with numerous lakes, rivers, and wetlands attracting large numbers of ducks.',
        'Mississippi provides outstanding duck hunting in the Delta region, with many public land opportunities.',
        'Missouri is a top duck hunting state, with flooded fields and wetlands along the Mississippi Flyway.',
        'Montana offers hunting in its prairie potholes and along rivers, though waterfowl numbers can be variable.',
        'Nebraska has great public land hunting, particularly along the Platte River during migration.',
        'Nevada has limited duck hunting, but certain wetlands provide hunting opportunities for dedicated hunters.',
        'New Hampshire offers a small window for duck hunting, primarily in coastal areas.',
        'New Jersey provides coastal marsh hunting along the Atlantic Flyway, though public access can be challenging.',
        'New Mexico has limited waterfowl habitats, but specific areas like the Rio Grande provide some hunting opportunities.',
        'New York offers diverse hunting environments, particularly in the Finger Lakes and along the Great Lakes.',
        'North Carolina has great hunting along the coast and in inland wetlands, especially in the Pamlico Sound.',
        'North Dakota is known for its prairie potholes, offering some of the best duck hunting in the country.',
        'Ohio provides good hunting along Lake Erie and its numerous inland marshes and reservoirs.',
        'Oklahoma offers solid hunting opportunities in wetlands and along rivers, especially during migration.',
        'Oregon provides diverse waterfowl hunting environments, from coastal estuaries to inland lakes.',
        'Pennsylvania offers hunting primarily in the northwest wetlands and along the Susquehanna River.',
        'Rhode Island has limited public hunting land, but coastal marshes provide some hunting opportunities.',
        'South Carolina offers great duck hunting along its coastal regions, with a variety of species.',
        'South Dakota has outstanding hunting in its prairie potholes and along the Missouri River.',
        'Tennessee provides excellent hunting, particularly in its western marshes and along the Mississippi Flyway.',
        'Texas is a premier duck hunting state, with a variety of habitats ranging from coastal marshes to inland lakes.',
        'Utah offers good hunting in its Great Salt Lake marshes and other wetlands throughout the state.',
        'Vermont has a shorter season, but provides hunting in its northern lakes and rivers.',
        'Virginia offers diverse hunting opportunities, especially in its coastal regions and along the Chesapeake Bay.',
        'Washington provides varied environments for hunting, from coastal bays to inland lakes and rivers.',
        'West Virginia has limited hunting opportunities, mostly focused around rivers and small wetlands.',
        'Wisconsin is a top waterfowl state, known for its duck hunting in the Great Lakes and inland wetlands.',
        'Wyoming offers hunting primarily in the eastern wetlands and along rivers, with variable duck populations.'
    ]
}


goat_sheep_hunting_data = {
    'State': ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'],
    'Score': [1, 10, 7, 1, 6, 9, 1, 1, 1, 1, 3, 9, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 9, 10, 1, 8, 8, 1, 6, 1, 1, 9, 1, 1, 7, 1, 1, 1, 9, 1, 6, 10, 1, 8, 9, 1, 1, 10],
    'Description': [
        'Alabama has no mountain goat or sheep populations, making hunting opportunities nonexistent.',
        'Alaska is the premier destination for mountain goat and sheep hunting, with vast wilderness areas and robust populations.',
        'Arizona offers opportunities for desert bighorn sheep hunting, though tags are difficult to draw, and populations are sparse.',
        'Arkansas does not have mountain goats or sheep, so hunting opportunities are unavailable.',
        'California has populations of bighorn sheep, particularly in desert regions, but hunting is heavily regulated with few tags available.',
        'Colorado offers excellent opportunities for Rocky Mountain bighorn sheep hunting, with challenging terrain and limited tag availability.',
        'Connecticut lacks mountainous terrain and does not have populations of mountain goats or sheep.',
        'Delaware is not known for mountain goat or sheep populations, so hunting is not available.',
        'Florida’s flat terrain and warm climate do not support mountain goat or sheep populations.',
        'Georgia has no populations of mountain goats or sheep, resulting in no hunting opportunities.',
        'Hawaii has some wild goats, but traditional mountain goat and sheep hunting as known in North America is limited.',
        'Idaho has great hunting for both mountain goats and bighorn sheep, with extensive public lands and rugged terrains.',
        'Illinois does not have mountainous terrain or populations of mountain goats or sheep.',
        'Indiana has no mountainous regions or populations of mountain goats or sheep, so hunting is not an option.',
        'Iowa lacks suitable habitat for mountain goats or sheep, resulting in no hunting opportunities.',
        'Kansas has no mountainous regions, hence no mountain goat or sheep populations.',
        'Kentucky does not offer mountain goat or sheep hunting due to a lack of suitable habitat.',
        'Louisiana’s flat terrain is unsuitable for mountain goats or sheep, resulting in no hunting opportunities.',
        'Maine has some rugged areas, but it does not have populations of mountain goats or sheep.',
        'Maryland lacks the mountainous regions necessary to support mountain goat or sheep populations.',
        'Massachusetts does not have suitable terrain or populations for mountain goat or sheep hunting.',
        'Michigan lacks the alpine environments needed for mountain goat or sheep populations.',
        'Minnesota’s terrain does not support mountain goat or sheep populations, so hunting is not available.',
        'Mississippi’s landscape does not support mountain goat or sheep populations.',
        'Missouri does not offer mountain goat or sheep hunting due to unsuitable terrain.',
        'Montana is known for its outstanding mountain goat and bighorn sheep populations, offering some of the best hunting in the lower 48 states.',
        'Nebraska lacks mountainous regions and thus does not have mountain goat or sheep hunting.',
        'Nevada provides hunting for desert bighorn sheep, though tags are rare and populations are managed closely.',
        'New Hampshire offers some bighorn sheep hunting, though opportunities are extremely limited and regulated.',
        'New Jersey does not have populations of mountain goats or sheep due to a lack of suitable habitat.',
        'New Mexico offers opportunities for desert bighorn sheep hunting, though tags are difficult to obtain, and populations are limited.',
        'New York has some rugged terrain, but it does not support mountain goat or sheep populations for hunting.',
        'North Carolina offers no mountain goat or sheep hunting due to unsuitable terrain.',
        'North Dakota has some rugged areas, but lacks the alpine environments for mountain goat or sheep populations.',
        'Ohio does not have the mountainous regions necessary for mountain goat or sheep populations.',
        'Oklahoma’s terrain is unsuitable for mountain goats or sheep, resulting in no hunting opportunities.',
        'Oregon has mountain goat and bighorn sheep hunting, though opportunities are limited with few tags and challenging terrain.',
        'Pennsylvania lacks the terrain and populations necessary for mountain goat or sheep hunting.',
        'Rhode Island does not have suitable habitat for mountain goats or sheep.',
        'South Carolina has no mountainous regions to support mountain goat or sheep populations.',
        'South Dakota has some sheep hunting opportunities in the Badlands, but they are extremely limited.',
        'Tennessee provides some hunting in its mountainous eastern regions, but opportunities are limited.',
        'Texas offers hunting for desert bighorn sheep and some exotic mountain goats, though tags can be costly and rare.',
        'Utah provides solid hunting for both mountain goats and bighorn sheep, with beautiful but rugged landscapes.',
        'Vermont does not have populations of mountain goats or sheep, making hunting unavailable.',
        'Virginia has some rugged terrain, but lacks populations of mountain goats or sheep.',
        'Washington has mountain goat hunting in its high alpine regions, though tag availability is limited.',
        'West Virginia has no known mountain goat or sheep populations, so hunting is not available.',
        'Wisconsin’s landscape is not suitable for mountain goats or sheep.',
        'Wyoming offers some of the best sheep and mountain goat hunting, with ample public lands and strong populations.'
    ]
}


bear_hunting_data = {
    'State': ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'],
    'Score': [1, 10, 7, 5, 8, 6, 3, 1, 5, 4, 1, 9, 2, 2, 1, 1, 3, 2, 9, 2, 3, 7, 8, 1, 2, 9, 1, 6, 8, 4, 7, 6, 7, 1, 2, 1, 9, 8, 1, 5, 3, 1, 7, 8, 7, 9, 8, 7, 9, 10],
    'Description': [
        'Alabama has no significant bear hunting opportunities due to a low bear population.',
        'Alaska offers world-class bear hunting, with both black and brown bears in vast wilderness areas.',
        'Arizona has a moderate black bear population, with hunting opportunities primarily in forested mountain regions.',
        'Arkansas provides some bear hunting, particularly in the Ozark and Ouachita National Forests, with a growing black bear population.',
        'California has a healthy black bear population, with diverse hunting environments in forests and mountains.',
        'Colorado offers bear hunting primarily in its mountainous regions, though hunting pressure can be high.',
        'Connecticut has a small black bear population, resulting in limited hunting opportunities.',
        'Delaware does not have a significant bear population, so bear hunting is not available.',
        'Florida has a limited bear hunting season due to conservation efforts and a small bear population.',
        'Georgia offers some bear hunting opportunities, particularly in the northern mountain regions and coastal areas.',
        'Hawaii does not have a native bear population, making bear hunting nonexistent.',
        'Idaho provides excellent bear hunting, with both spring and fall seasons in its rugged mountain terrains.',
        'Illinois does not have a significant bear population, resulting in no hunting opportunities.',
        'Indiana has no established bear population, making bear hunting unavailable.',
        'Iowa lacks suitable habitat for bears, resulting in no bear hunting opportunities.',
        'Kansas does not have a bear population, hence no hunting opportunities.',
        'Kentucky has a small but growing bear population, primarily in the eastern mountainous regions.',
        'Louisiana’s habitat does not support a significant bear population, making hunting opportunities rare.',
        'Maine is known for its strong black bear population, offering both spring and fall hunting seasons.',
        'Maryland has a small bear population, with limited hunting opportunities in specific areas.',
        'Massachusetts has a growing bear population, but hunting opportunities are limited and heavily regulated.',
        'Michigan offers excellent bear hunting, particularly in the Upper Peninsula, with diverse habitats and a robust population.',
        'Minnesota provides great bear hunting, especially in the northern forests, with a healthy population.',
        'Mississippi’s bear population is low, resulting in no dedicated bear hunting seasons.',
        'Missouri has no established bear hunting due to a small and protected bear population.',
        'Montana offers top-tier bear hunting opportunities, with both black and grizzly bears in its vast wilderness areas.',
        'Nebraska lacks a significant bear population, resulting in no bear hunting opportunities.',
        'Nevada has some bear hunting in the western mountain ranges, but opportunities are limited and closely regulated.',
        'New Hampshire offers bear hunting in its northern forests, with a healthy and well-managed bear population.',
        'New Jersey has a growing bear population, with regulated hunting seasons to manage numbers.',
        'New Mexico provides bear hunting primarily in its forested and mountainous regions, with both spring and fall seasons.',
        'New York offers bear hunting in its Adirondack and Catskill regions, with a healthy black bear population.',
        'North Carolina has strong bear hunting opportunities, particularly in its coastal and mountainous areas.',
        'North Dakota has no significant bear population, so hunting opportunities are nonexistent.',
        'Ohio has a small bear population, making hunting opportunities rare and heavily regulated.',
        'Oklahoma lacks a significant bear population, resulting in no dedicated hunting seasons.',
        'Oregon offers excellent bear hunting, with a variety of habitats and both spring and fall seasons.',
        'Pennsylvania has a well-managed bear population, offering quality hunting opportunities in forested regions.',
        'Rhode Island does not have an established bear population, resulting in no hunting opportunities.',
        'South Carolina has some bear hunting, primarily in the coastal and mountainous regions.',
        'South Dakota has a minimal bear population, making bear hunting opportunities scarce.',
        'Tennessee has growing bear populations in the eastern mountainous regions, with regulated hunting seasons.',
        'Texas does not have a native bear hunting season, as bears are rare and protected in the state.',
        'Utah provides bear hunting opportunities in its forested and mountainous areas, though hunting is closely regulated.',
        'Vermont offers quality bear hunting in its northern forests, with a healthy and well-managed population.',
        'Virginia has a strong bear population, offering hunting in various regions, particularly in the western mountains.',
        'Washington provides both spring and fall bear hunting seasons, with diverse habitats across the state.',
        'West Virginia has a healthy bear population, with ample hunting opportunities in its mountainous terrain.',
        'Wisconsin is known for its robust bear population, particularly in the northern forests, offering high-quality hunting.',
        'Wyoming provides world-class bear hunting, with both black and grizzly bears in rugged mountain areas.'
    ]
}


turkey_hunting_data = {
    'State': ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'],
    'Score': [9, 3, 6, 8, 4, 7, 5, 4, 9, 10, 2, 7, 8, 8, 7, 8, 9, 7, 5, 6, 4, 8, 8, 9, 9, 8, 8, 3, 5, 4, 6, 7, 8, 6, 9, 9, 5, 9, 4, 9, 9, 8, 10, 7, 6, 8, 5, 9, 9, 8],
    'Description': [
        'Alabama offers fantastic turkey hunting opportunities with large public land areas and a healthy turkey population.',
        'Alaska provides unique hunting experiences, but turkeys are not native to the region, making hunting opportunities scarce.',
        'Arizona has decent turkey populations in specific regions, with beautiful hunting terrain, though public access can be limited.',
        'Arkansas provides excellent turkey hunting, with access to public lands and varied habitats for hunters.',
        'California has diverse landscapes for hunting, but turkey populations and public access can be limited in some areas.',
        'Colorado offers quality turkey hunting with both Merriam’s and Rio Grande turkeys, particularly in the eastern plains.',
        'Connecticut has moderate turkey populations, but public hunting lands are limited and highly regulated.',
        'Delaware has small but manageable turkey populations, with limited public hunting opportunities.',
        'Florida is renowned for its Osceola turkeys, offering a unique hunting experience in swampy terrains.',
        'Georgia is one of the top turkey hunting states with abundant populations and varied habitats.',
        'Hawaii offers unique hunting experiences, though turkeys are less common and hunting is less popular.',
        'Idaho provides quality hunting for Merriam’s turkeys, particularly in its forested northern regions.',
        'Illinois has a healthy turkey population, with good hunting opportunities on both public and private lands.',
        'Indiana offers solid turkey hunting with a well-managed population and a mix of public and private lands.',
        'Iowa provides a rewarding turkey hunting experience, though hunting is primarily on private land.',
        'Kansas has diverse habitats and a strong turkey population, making it one of the best states for turkey hunting.',
        'Kentucky is known for its large turkey population and vast public lands, offering excellent hunting opportunities.',
        'Louisiana provides good turkey hunting with varied terrain, although public land can be crowded during the season.',
        'Maine has a growing turkey population, providing a rugged hunting experience in its forested regions.',
        'Maryland offers solid turkey hunting, though public land access can be somewhat limited.',
        'Massachusetts has a decent turkey population, but public land hunting opportunities are limited and highly regulated.',
        'Michigan has a strong turkey population with abundant public lands, although hunting pressure can be high.',
        'Minnesota offers a great turkey hunting experience with a mix of public lands and varied habitats.',
        'Mississippi is a top state for turkey hunting, known for its abundant population and public land opportunities.',
        'Missouri provides some of the best turkey hunting with large populations and a variety of habitats.',
        'Montana has good turkey hunting opportunities, particularly in the eastern and central parts of the state.',
        'Nebraska offers excellent turkey hunting, with three subspecies available and plenty of public land.',
        'Nevada has limited turkey hunting opportunities due to its desert terrain and lower turkey populations.',
        'New Hampshire provides a challenging hunt in forested terrain, though turkey populations are smaller.',
        'New Jersey has a decent turkey population but limited public land and heavy regulations.',
        'New Mexico offers scenic turkey hunting, though the turkey population is more scattered in the state’s rugged terrain.',
        'New York provides a variety of hunting environments with a healthy turkey population and good public land access.',
        'North Carolina offers solid turkey hunting with extensive public lands and a well-managed population.',
        'North Dakota provides good hunting with less pressure, although turkey populations are more localized.',
        'Ohio is known for its strong turkey population and good public hunting lands, though hunting pressure can be intense.',
        'Oklahoma has diverse turkey habitats and a mix of public and private land hunting opportunities.',
        'Oregon offers varied hunting environments, with a mix of public lands and multiple turkey subspecies.',
        'Pennsylvania has an excellent turkey population and abundant public land, although hunting pressure is high.',
        'Rhode Island has limited public hunting land and a smaller turkey population.',
        'South Carolina offers a traditional turkey hunting experience with varied terrain, though public access can be limited.',
        'South Dakota provides great turkey hunting with abundant public land and less hunting pressure.',
        'Tennessee is known for its healthy turkey population and various public lands, offering a quality hunting experience.',
        'Texas is famous for its turkey hunting, with diverse environments and large ranches offering prime opportunities.',
        'Utah offers scenic hunting opportunities, though turkey populations can be variable.',
        'Vermont provides a classic turkey hunting experience in dense forests, though turkey populations are smaller.',
        'Virginia has strong turkey hunting on public lands with a healthy population and moderate hunting pressure.',
        'Washington offers varied hunting terrains, though turkey populations are more concentrated in specific regions.',
        'West Virginia boasts a large turkey population and public lands, offering a quality hunting experience.',
        'Wisconsin is known for its excellent turkey hunting and diverse environments, although hunting pressure can be high.',
        'Wyoming provides fantastic hunting in scenic areas, though turkey populations are more localized.'
    ]
}


hog_hunting_data = {
    'State': ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'],
    'Score': [9, 1, 3, 8, 5, 4, 1, 1, 10, 10, 2, 2, 3, 2, 1, 2, 7, 9, 1, 2, 1, 2, 2, 10, 8, 1, 2, 1, 1, 1, 4, 1, 8, 1, 2, 9, 3, 2, 1, 9, 2, 9, 10, 2, 1, 8, 2, 2, 2, 1],
    'Description': [
        'Alabama has a large feral hog population, with many public lands offering year-round hunting opportunities.',
        'Alaska has virtually no feral hog presence due to its climate and terrain, making hog hunting non-existent.',
        'Arizona has some feral hog populations, but they are sparse and found mostly on private lands.',
        'Arkansas has a significant feral hog population with hunting opportunities on public lands, though regulations apply.',
        'California has feral hogs across various regions, but hunting is heavily regulated, and public land access is limited.',
        'Colorado has a small feral hog population primarily on private lands, with limited public hunting opportunities.',
        'Connecticut has no significant feral hog population, resulting in no dedicated hog hunting opportunities.',
        'Delaware has no known feral hog populations, so hunting opportunities are practically nonexistent.',
        'Florida is a top destination for hog hunting, with vast populations and numerous public land hunting opportunities year-round.',
        'Georgia boasts a large hog population and offers excellent hunting opportunities on both public and private lands.',
        'Hawaii has feral hogs, particularly on some islands, offering unique hunting experiences in dense tropical forests.',
        'Idaho has a minimal feral hog presence, mostly confined to private lands, limiting hunting opportunities.',
        'Illinois has some feral hogs, but they are primarily located on private lands with limited public hunting access.',
        'Indiana has a small, scattered feral hog population, resulting in limited hunting opportunities.',
        'Iowa has virtually no feral hog presence, so dedicated hog hunting opportunities are scarce.',
        'Kansas has a minor feral hog population mainly found on private lands, limiting hunting access.',
        'Kentucky offers decent hog hunting opportunities, particularly in the southern regions with known hog populations.',
        'Louisiana is known for its large hog population and offers extensive public land hunting opportunities.',
        'Maine has no significant feral hog population, so hog hunting is not a popular activity.',
        'Maryland has a very small feral hog presence, resulting in limited hunting opportunities.',
        'Massachusetts has no known feral hog populations, making hog hunting practically nonexistent.',
        'Michigan has some hog populations, but they are scattered, and hunting opportunities are mostly on private lands.',
        'Minnesota has a minimal feral hog presence, resulting in very limited hunting opportunities.',
        'Mississippi is a prime location for hog hunting, with abundant populations and public land access.',
        'Missouri has a notable hog population, particularly in the southern regions, offering good hunting on public lands.',
        'Montana has no significant feral hog populations, so dedicated hunting opportunities are absent.',
        'Nebraska has a minimal feral hog presence, with limited hunting opportunities mostly on private lands.',
        'Nevada has very few feral hogs, making hog hunting opportunities almost nonexistent.',
        'New Hampshire has no known feral hog populations, leading to a lack of hunting opportunities.',
        'New Jersey has a very small feral hog presence, with little to no dedicated hunting opportunities.',
        'New Mexico has some hog populations, primarily on private lands, with hunting opportunities limited to specific areas.',
        'New York has a minimal feral hog presence, leading to limited hunting opportunities.',
        'North Carolina has a sizeable feral hog population, providing good hunting opportunities on public lands.',
        'North Dakota has virtually no feral hog population, resulting in no dedicated hunting activities.',
        'Ohio has a minor feral hog presence, mainly confined to private lands, restricting hunting opportunities.',
        'Oklahoma is a prime state for hog hunting, with abundant populations and access to public and private lands.',
        'Oregon has scattered hog populations, with hunting opportunities primarily on private lands.',
        'Pennsylvania has a very small feral hog population, resulting in limited hunting opportunities.',
        'Rhode Island has no known feral hog populations, making hog hunting nonexistent.',
        'South Carolina offers excellent hog hunting opportunities, with many public lands and a healthy hog population.',
        'South Dakota has virtually no feral hog presence, leading to a lack of dedicated hunting opportunities.',
        'Tennessee is known for its large feral hog population, providing excellent hunting on both public and private lands.',
        'Texas is the top destination for hog hunting, with millions of hogs and ample public and private land hunting opportunities.',
        'Utah has a small feral hog population, resulting in limited hunting opportunities mostly on private lands.',
        'Vermont has no significant feral hog population, making hog hunting practically nonexistent.',
        'Virginia offers good hog hunting opportunities, especially in the southeastern regions with established populations.',
        'Washington has a very small feral hog presence, leading to limited hunting opportunities.',
        'West Virginia has scattered hog populations, offering some hunting opportunities, primarily on private lands.',
        'Wisconsin has a very small feral hog population, resulting in minimal hunting opportunities.',
        'Wyoming has no known feral hog populations, making hog hunting nonexistent.'
    ]
}


hunting_data = {
    'deer': deer_hunting_data,
    'goat / sheep': goat_sheep_hunting_data,
    'bear': bear_hunting_data,
    'duck': duck_hunting_data,
    'turkey': turkey_hunting_data,
    'hog': hog_hunting_data
}

# Function to plot a hunting quality map for a given species
def plot_hunting_map(species):
    if species not in hunting_data:
        st.write(f"No data available for {species}.")
        return

    # Get the data for the selected species
    data = hunting_data[species]

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Create the choropleth map using Plotly
    fig = px.choropleth(
        df,
        locations='State',
        locationmode='USA-states',
        color='Score',
        scope='usa',
        color_continuous_scale=hex_colors_with_light_gray,  # Use the custom color scale
        hover_name='State',
        hover_data={'Description': True, 'Score': True},
        labels={'Score': f'{species.capitalize()} Hunting Quality'}
    )

    # Customize layout
    fig.update_layout(
        title_text=f'Quality of {species.capitalize()} Hunting in the USA by State',
        geo=dict(lakecolor='rgb(255, 255, 255)'),
        font=dict(family='Arial, sans-serif', size=14, color='black')
    )

    # Display the map in Streamlit
    st.plotly_chart(fig)

# Streamlit app
def main():
    st.title('Hunting Quality Map in the USA')
    st.sidebar.header('Select Hunting Species')
    
    # Species selection dropdown
    species_to_display = st.sidebar.selectbox('Choose a species:', list(hunting_data.keys()), index=0)

    # Plot the map for the selected species
    plot_hunting_map(species_to_display)

if __name__ == '__main__':
    main()
