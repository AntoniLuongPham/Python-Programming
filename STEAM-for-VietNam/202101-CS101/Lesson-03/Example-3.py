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
    first = 0
    last = len(profile_list) - 1
    while first <= last:
        mid = int((first + last) / 2)
        mid_profile = profile_list[mid]
        if keyword > mid_profile["name"]:
            first = mid + 1
        elif keyword < mid_profile["name"]:
            last = mid - 1
        else:
            return mid_profile


print("== TIM KIEM HO SO ==")
keyword = input("Input a name: ")
profile = search_profile(keyword)
print(profile)
