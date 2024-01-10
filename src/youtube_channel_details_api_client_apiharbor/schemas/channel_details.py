from .base import BaseModelORM


from typing import Any, List, Optional

from pydantic import BaseModel

class LinkAlternate(BaseModel):
    hrefUrl: str


class Thumbnail(BaseModel):
    url: str
    width: int
    height: int


class Banner(BaseModel):
    thumbnails: List[Thumbnail]


class SocialMediaUrls(BaseModel):
    vimeo_urls: List
    medium_urls: List
    pinterest_urls: List
    vine_urls: List
    patreon_urls: List
    unclassified_urls: List
    discord_urls: List
    sound_cloud_urls: List
    spotify_urls: List[str]
    onlyfans_urls: List
    twitch_urls: List
    tik_tok_urls: List
    tumblr_urls: List
    reddit_urls: List
    linkedin_urls: List
    facebook_urls: List
    twitter_urls: List
    instagram_urls: List


class Data(BaseModel):
    channel_url: str
    channel_name: str
    channel_id: str
    joined_date_text: str
    channel_country: str
    rss_url: str
    channel_emails: List[str]
    is_verified_category: bool
    channel_view_count: int
    channel_subscriber_count: int
    channel_video_count: int
    description: str
    link_alternates: List[LinkAlternate]
    tracking_params: str
    is_family_safe: bool
    keywords: List[str]
    facebook_profile_id: Any
    available_countries: List[str]
    url_twitter_ios: str
    url_applinks_ios: str
    ios_app_store_id: str
    ios_app_arguments: str
    app_name: str
    android_packgage: str
    android_link: str
    banner: Banner
    badges: List[str]
    avatar_url: str
    social_media_urls: SocialMediaUrls


class ChannelDetails(BaseModelORM):
    status: int
    description: str
    data: Data