# مدل ساده تستی بدون یادگیری ماشین، فقط برای نمایش ساختار
def get_response(text):
    responses = {
        "سلام": "سلام! حالت چطوره؟",
        "اسم تو چیه؟": "من یه مدل تستی ساده‌ام!",
        "خداحافظ": "فعلاً!",
    }
    return responses.get(text, "متأسفم، متوجه نشدم چی گفتی.")
