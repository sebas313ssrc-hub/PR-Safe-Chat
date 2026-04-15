import streamlit as st
import urllib.parse

phone_number = "19399697275"

month_safety_data = {
    "january": {
        "summary": "Cooler, drier month with good beach and hiking conditions. Stronger surf on north coasts.",
        "tips": [
            "Watch for strong rip currents on the north and northwest coasts.",
            "Pack a light layer for breezy evenings.",
            "Expect more crowds due to winter tourism."
        ]
    },
    "february": {
        "summary": "Pleasant temps, low rain, great for outdoor activities.",
        "tips": [
            "Check beach safety flags for surf conditions.",
            "Book transportation early in popular areas.",
            "Use sunscreen even on cloudy days."
        ]
    },
    "march": {
        "summary": "Dry and warm, popular for spring travel.",
        "tips": [
            "Hydrate well during midday heat.",
            "Stay on marked trails in El Yunque.",
            "Expect more traffic around spring break."
        ]
    },
    "april": {
        "summary": "Hotter days and rising humidity.",
        "tips": [
            "Avoid strenuous activity during peak heat.",
            "Carry insect repellent.",
            "Watch for passing thunderstorms."
        ]
    },
    "may": {
        "summary": "Hot, humid, and more frequent showers.",
        "tips": [
            "Avoid rivers and waterfalls after rain.",
            "Wear breathable clothing.",
            "Protect valuables from sudden downpours."
        ]
    },
    "june": {
        "summary": "Start of hurricane season; hot and humid.",
        "tips": [
            "Monitor tropical weather updates.",
            "Know your accommodation’s storm procedures.",
            "Avoid swimming in rivers after heavy rain."
        ]
    },
    "july": {
        "summary": "Peak summer heat and active hurricane season.",
        "tips": [
            "Check daily weather forecasts.",
            "Use high‑SPF sunscreen.",
            "Expect heavier traffic and crowds."
        ]
    },
    "august": {
        "summary": "Very hot and one of the most active hurricane months.",
        "tips": [
            "Monitor National Hurricane Center updates.",
            "Confirm storm procedures with your lodging.",
            "Avoid ocean swimming during rough surf."
        ]
    },
    "september": {
        "summary": "Peak of hurricane season; very hot and humid.",
        "tips": [
            "Consider travel insurance for weather disruptions.",
            "Follow local guidance during storms.",
            "Keep offline maps and a small emergency kit."
        ]
    },
    "october": {
        "summary": "Hurricane risk decreases but still present.",
        "tips": [
            "Monitor tropical weather early in the month.",
            "Expect heavy showers.",
            "Drive carefully during rain due to flooding."
        ]
    },
    "november": {
        "summary": "End of hurricane season; warm and pleasant.",
        "tips": [
            "Early November may still see storms.",
            "Use sun protection.",
            "Holiday travel increases later in the month."
        ]
    },
    "december": {
        "summary": "Comfortable temps and drier conditions.",
        "tips": [
            "Expect crowds in tourist areas.",
            "Book tours in advance.",
            "Stay aware of surroundings during nightlife."
        ]
    }
}

# ✅ FIX: Function moved OUTSIDE the button
def get_pr_safety_info(month_input: str) -> dict | None:
    month_input = month_input.strip().lower()

    month_map = {
        "jan": "january", "january": "january",
        "feb": "february", "february": "february",
        "mar": "march", "march": "march",
        "apr": "april", "april": "april",
        "may": "may",
        "jun": "june", "june": "june",
        "jul": "july", "july": "july",
        "aug": "august", "august": "august",
        "sep": "september", "sept": "september", "september": "september",
        "oct": "october", "october": "october",
        "nov": "november", "november": "november",
        "dec": "december", "december": "december"
    }

    normalized = month_map.get(month_input)
    if not normalized:
        return None

    return {
        "month": normalized,
        "summary": month_safety_data[normalized]["summary"],
        "tips": month_safety_data[normalized]["tips"]
    }


st.image("PR_Safe_Chat.png", caption="Created using Canva")

name = st.text_input("Enter your name")

if st.button("Click Me to Enter"):
    st.session_state["entered"] = True

if st.session_state.get("entered"):
    st.write(f"Hello, {name}!\n\n I am PR Safe Chat!")
    st.write(f" 🌴 Planning a Trip to Puerto Rico \n\n I Can Help!\n\n {name} please tell me the month you’re visiting, and I’ll share the most important safety tips for that time of year — including weather conditions, seasonal events, and anything else that can help you enjoy a smooth and safe vacation in Puerto Rico. Just let me know your travel month and I’ll take it from there.")

    month = st.text_input("Enter the month you’re visiting")

    if st.button("Enter"):
        st.session_state["month_entered"] = True

    if st.session_state.get("month_entered"):
        info = get_pr_safety_info(month)

        if info:
            st.image("Safety_Tips.png", caption="Created using Canva")
            st.subheader(f"Safety Tips for {info['month'].title()}")
            st.write(info["summary"])
            st.write("### Key Tips:")
            for tip in info["tips"]:
                st.write(f"- {tip}")

            st.write(" \n\n\n\n ")

            if st.button("'Click Me' When you get to Puerto Rico"):
                st.session_state["in_pr"] = True

            if st.session_state.get("in_pr"):
                st.image("important.png", caption="Created using Canva")
                st.write(""" 
🌴 Welcome to Puerto Rico! Here’s What You Should Know to Stay Safe During Your Visit

Thanks for choosing Puerto Rico as your vacation destination. This island is full of beauty, culture, and adventure, and I want to help you enjoy it all with peace of mind. Here are some important safety tips to keep in mind during your stay:

🌦 **Weather & Natural Conditions**
- Puerto Rico is in a tropical climate, so expect sudden rain showers and strong sun. Stay hydrated and use sunscreen.
- Hurricane season runs from June to November. If you’re visiting during this time, keep an eye on weather updates and follow local guidance.
- Beaches can have strong currents, especially on the north and west coasts. Swim only in designated safe areas and follow lifeguard instructions when available.

🛟 Safest and Calmest Beaches (Ideal for swimming):  
- Playa Caracas (Vieques): Known for its crystal‑clear, calm waters and family‑friendly vibe.
- Playa Combate (Cabo Rojo): Calm, shallow waters on the southwest coast.
- Boquerón Beach (Cabo Rojo): Large beach with protected areas and available services.
- Isla Verde (Carolina): Very popular, with wide swimming areas and lifeguards.
- Punta Guilarte Beach (Arroyo): Southern coast, calm waters.

⚠️ Most Dangerous Beaches (High risk of rip currents):  
- Mar Chiquita (Manatí): Beautiful but has a dangerous opening to the open sea.
- Poza de las Mujeres (Manatí): Known for unpredictable, strong currents.
- Guajataca Beach (Quebradillas): Famous for its strong currents.
- Playa Escondida (Fajardo): High risk of strong currents.

‼️ Please remember that any beach can be dangerous do to many factors and you should always have precaution when swiming ‼️

🚗 **Transportation & Driving**
- Roads can be narrow, busy, or winding, especially in rural areas. Drive carefully and avoid nighttime travel in unfamiliar places.
- If you’re renting a car, always lock your doors and avoid leaving valuables inside.
- Rideshare services and taxis are widely available in major cities.

🏙 **Urban Safety**
- Puerto Rico is generally safe for tourists, but like any destination, it’s smart to stay aware of your surroundings.
- Stick to well‑lit, populated areas at night.
- Keep personal belongings secure and avoid displaying expensive items in crowded places.

🌊 **Outdoor Adventures**
- If you’re hiking, especially in El Yunque or other forest areas, stay on marked trails and check conditions before heading out.
- Rivers and waterfalls can become dangerous quickly after rain. Avoid swimming during or right after heavy rainfall.

🍽 **Food & Water**
- Tap water in Puerto Rico is treated and safe to drink.
- Street food is popular and delicious—just choose vendors with good hygiene and steady customer flow.

📞 **Emergency Information**
- Dial 911 for emergencies.
- Many locals speak English, especially in tourist areas, but having a translation app can be helpful. """)

            st.write(" Or send a message via whatsapp to get info.")

            default_message = "I have arrived to Puerto Rico."

            message = st.text_area("Your message", default_message)
            encoded_message = urllib.parse.quote(message)

            whatsapp_url = f"https://wa.me/{phone_number}?text={encoded_message}"

            if st.button("Send via WhatsApp"):
                st.markdown(
                    f'<a href="{whatsapp_url}" target="_blank">Click here to open WhatsApp</a>',
                    unsafe_allow_html=True
                )

        else:
            st.error("Invalid month. Try again.")
