#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SocialInfoView import SocialInfoView


class AlipayUserSocialinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserSocialinfoQueryResponse, self).__init__()
        self._social_info_views = None

    @property
    def social_info_views(self):
        return self._social_info_views

    @social_info_views.setter
    def social_info_views(self, value):
        if isinstance(value, list):
            self._social_info_views = list()
            for i in value:
                if isinstance(i, SocialInfoView):
                    self._social_info_views.append(i)
                else:
                    self._social_info_views.append(SocialInfoView.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayUserSocialinfoQueryResponse, self).parse_response_content(response_content)
        if 'social_info_views' in response:
            self.social_info_views = response['social_info_views']
