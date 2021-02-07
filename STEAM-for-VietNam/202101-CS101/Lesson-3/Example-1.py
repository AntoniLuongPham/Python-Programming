duc_ngo_profile = {
    "name": "Duc Ngo",
    "job": "Software Development Engineer",
    "org": "Google"
}

harry_doan_profile = {
    "name": "Harry Doan",
    "job": "Software Development Engineer",
    "org": "CZI"
}

ken_nguyen_profile = {
    "name": "Ken Nguyen",
    "job": "Software Development Engineer",
    "org": "Amazon"
}

zi_vu_profile = {
    "name": "Zi Vu",
    "job": "Software Development Engineer",
    "org": "Twitter"
}

profile_list = [
    duc_ngo_profile,
    harry_doan_profile,
    ken_nguyen_profile,
    zi_vu_profile
]


def search_profile(keyword):
    for profile in profile_list:
        if keyword == profile["name"]:
            return profile


print("== TIM KIEM HO SO ==")
keyword = input("Input a name: ")
profile = search_profile(keyword)
print(profile)
