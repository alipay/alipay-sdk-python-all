#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AvatarAsianAssetVO import AvatarAsianAssetVO


class AlipayUserAccountZavatarOwnedassetsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAccountZavatarOwnedassetsQueryResponse, self).__init__()
        self._avatar_asset_suit_v_os = None

    @property
    def avatar_asset_suit_v_os(self):
        return self._avatar_asset_suit_v_os

    @avatar_asset_suit_v_os.setter
    def avatar_asset_suit_v_os(self, value):
        if isinstance(value, list):
            self._avatar_asset_suit_v_os = list()
            for i in value:
                if isinstance(i, AvatarAsianAssetVO):
                    self._avatar_asset_suit_v_os.append(i)
                else:
                    self._avatar_asset_suit_v_os.append(AvatarAsianAssetVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayUserAccountZavatarOwnedassetsQueryResponse, self).parse_response_content(response_content)
        if 'avatar_asset_suit_v_os' in response:
            self.avatar_asset_suit_v_os = response['avatar_asset_suit_v_os']
