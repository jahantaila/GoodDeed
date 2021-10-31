# GoodDeed
## _Eradicating poverty and world hunger by connecting people in need and donors_




GoodDeed is a user-driven, django based web application
that allows donors to donate food and supplies to people in 
need and get rewarded while doing so. GoodDeed contains
many features that allow donors to benefit from their 
donations, giving them a sense of motivation and an 
incentive to donate again. Bellow you will find all of
the details and features that GoodDeed incorporates  to 
make sure users have an outstanding expirence. Thank 
you for choosing GoodDeed.
----

## Features

- Advanced donation and request system
- Dynamically styled and easy-to-use UI
- Games and other incentives for donating
- Advanced Maps through Leaflet, Google Maps, and OpenStreetMaps
- Custom made databases, stores user's data safely and securely
- Modern Bootstrap enhanced dasboard
- Community leaderboards 
- Weekly events & competitions
- Friendly community
- Updated news panels

GoodDeed was created to provide ease and efficency
into donating supplies to food banks and the  less 
fortunate

> The overriding design goal for GoodDeed
> is to make it as easy to use as possible. 
> The idea is that anyone should be able
> to donate to food banks and the less
> fortunate, with the ease and efficency 
> from their own home. 


Bellow is a guide that goes in-depth about the various
features that GoodDeed offers. 

## Donating 

Navigating [here](/donate/) will take you to the donation screen. You should be able to see a form, which you need to fill out in order for your donation to be added to our database. Please follow the instructions bellow, and your donation will be posted in a tentetive manner. 

    1. Title: Please fill out the title of your donation. This should be the item you are donating 
    2. Phone Number: Please type in your phone number. You will only be contacted in the event that someone accepts your donation. 
    3. Category: From the drop down menu, please select a category that your donation fits into.
    4. Quantity: Please include the quantity of the items you are donating. 
    5. Location: Please include the location for someone to pick up your donation at. 
    6. Image: Please upload an image of your donation. 
    7. Description: Please include a short description of the item you are donating

And thats it! If you did everything correctly, you will be taken to a thank you page. 
You can then navigate to your dashboard. You should have recieved points, and 
your donation has been added to the database. You can view your donation by clicking 
on [Availible Supplies](/availablesupplies/), and scrolling down until you see your donation.

**PLEASE NOTE: GoodDeed saves all user data in a secure custom database, but as an added
security mesure we do not allow users to see your location. If someone is interested in your 
donation, they will be able to see your phone number, and they will contact you. It is your job
to disclose when and where someone should come to pick up your donation.**



## Requests

Navigating [here](/request/) will take you to the request screen. You should be able to see a form, which you need to fill out in order for your request to be added to the GoodDeed database. **Before you request an item, please check  [Availible Supplies](/availablesupplies/) to make sure the item you are requesting is not already availible. Users who violate this may be at risk of getting banned**

While filling out this form, please try to make it as discrete as possible. Remember: You are requesting an item from a donor or organization, and the GoodDeed algorithm tends to overlook low-detailed requests. Please follow the instructions bellow, and your request will be posted. 

    1. Title: Please fill out the title of your request. This should be the item you are requesting 
    2. Phone Number: Please type in your phone number. You will only be contacted in the event that someone accepts your request. 
    3. Category: From the drop down menu, please select a category that your request best fits into.
    4. Quantity: Please include the quantity of the items you are requesting. 
    5. Location: Please include your location, which will be used in the event that someone accepts your request. 
    6. Image: Please upload an image of your request. This is collected as a reference to donors . 
    7. Description: Please include a short description of the item you are requesting. Specify certain brands/packages. 


And thats it! If you did everything correctly, you will be redirected to your user- dashboard. 
If you did not get an error, your request should have sucsesfully been added to the database.  
You can view your request by clicking on [Outgoing Requests](/outgoingrequests/), and scrolling down until you see
your request.

**PLEASE NOTE: GoodDeed saves all user data in a secure custom database, but as an added
security mesure we do not allow users to see your location. If someone is interested in your 
request, they will be able to see your phone number, and they will contact you. It is your job
to disclose when and where someone should drop of their donation.**



## Incentives/Games

GoodDeed rewards donors with points for donating and accepting requests.
This is a unique feature, and no other donation application have this feature. 
Bellow are details about the rates that donating and accepting requests give, 
and the different amount of points you need to accsess certain perks. 


##### Donation Point Rates: 
`UserDetail.objects.filter(user=request.user).update(points=F('points') + (quantity * 2))`


##### Request Point Rates: 
`UserDetail.objects.filter(user=request.user).update(points=F('points') + (quantity * 2) + 100)`
    

#### Points to perk ratio: 

	
	
| Points | Perk |
| ------ | ------ |
| 100 | Accsess to [Fun & More](/fun/) |
| 500 | Accsess to games  |
| 1000 | Accsess to global leaderboards |
| 5000 | Faster requests, skip donation queues  |
| 10000 | Accsess to new games |
| 50000 | Become verified, new perks |

**Please note that these are just the base perks, new perks are created 
and awarded weekly. Check the news tab for more**

## About the Creator

GoodDeed was created by Jahan Taila, a high school student at Dupont Manual High School. You can contact him at tailajahan@gmail.com



