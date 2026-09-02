#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EpAssistantServiceSubtitleSegment import EpAssistantServiceSubtitleSegment


class ZhimaCreditEpAssistantServicecardQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpAssistantServicecardQueryResponse, self).__init__()
        self._badge_jump_url = None
        self._badge_notify_type = None
        self._badge_text = None
        self._badge_type = None
        self._button_text = None
        self._card_jump_url = None
        self._card_notification_id = None
        self._card_notify_type = None
        self._card_subtitle = None
        self._card_title = None
        self._guide_scene = None
        self._potential_benefits = None

    @property
    def badge_jump_url(self):
        return self._badge_jump_url

    @badge_jump_url.setter
    def badge_jump_url(self, value):
        self._badge_jump_url = value
    @property
    def badge_notify_type(self):
        return self._badge_notify_type

    @badge_notify_type.setter
    def badge_notify_type(self, value):
        self._badge_notify_type = value
    @property
    def badge_text(self):
        return self._badge_text

    @badge_text.setter
    def badge_text(self, value):
        self._badge_text = value
    @property
    def badge_type(self):
        return self._badge_type

    @badge_type.setter
    def badge_type(self, value):
        self._badge_type = value
    @property
    def button_text(self):
        return self._button_text

    @button_text.setter
    def button_text(self, value):
        self._button_text = value
    @property
    def card_jump_url(self):
        return self._card_jump_url

    @card_jump_url.setter
    def card_jump_url(self, value):
        self._card_jump_url = value
    @property
    def card_notification_id(self):
        return self._card_notification_id

    @card_notification_id.setter
    def card_notification_id(self, value):
        self._card_notification_id = value
    @property
    def card_notify_type(self):
        return self._card_notify_type

    @card_notify_type.setter
    def card_notify_type(self, value):
        self._card_notify_type = value
    @property
    def card_subtitle(self):
        return self._card_subtitle

    @card_subtitle.setter
    def card_subtitle(self, value):
        if isinstance(value, list):
            self._card_subtitle = list()
            for i in value:
                if isinstance(i, EpAssistantServiceSubtitleSegment):
                    self._card_subtitle.append(i)
                else:
                    self._card_subtitle.append(EpAssistantServiceSubtitleSegment.from_alipay_dict(i))
    @property
    def card_title(self):
        return self._card_title

    @card_title.setter
    def card_title(self, value):
        self._card_title = value
    @property
    def guide_scene(self):
        return self._guide_scene

    @guide_scene.setter
    def guide_scene(self, value):
        self._guide_scene = value
    @property
    def potential_benefits(self):
        return self._potential_benefits

    @potential_benefits.setter
    def potential_benefits(self, value):
        if isinstance(value, list):
            self._potential_benefits = list()
            for i in value:
                self._potential_benefits.append(i)

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpAssistantServicecardQueryResponse, self).parse_response_content(response_content)
        if 'badge_jump_url' in response:
            self.badge_jump_url = response['badge_jump_url']
        if 'badge_notify_type' in response:
            self.badge_notify_type = response['badge_notify_type']
        if 'badge_text' in response:
            self.badge_text = response['badge_text']
        if 'badge_type' in response:
            self.badge_type = response['badge_type']
        if 'button_text' in response:
            self.button_text = response['button_text']
        if 'card_jump_url' in response:
            self.card_jump_url = response['card_jump_url']
        if 'card_notification_id' in response:
            self.card_notification_id = response['card_notification_id']
        if 'card_notify_type' in response:
            self.card_notify_type = response['card_notify_type']
        if 'card_subtitle' in response:
            self.card_subtitle = response['card_subtitle']
        if 'card_title' in response:
            self.card_title = response['card_title']
        if 'guide_scene' in response:
            self.guide_scene = response['guide_scene']
        if 'potential_benefits' in response:
            self.potential_benefits = response['potential_benefits']
