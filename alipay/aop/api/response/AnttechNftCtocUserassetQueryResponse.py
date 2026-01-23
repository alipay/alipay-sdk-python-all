#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserOwnedAsset import UserOwnedAsset


class AnttechNftCtocUserassetQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftCtocUserassetQueryResponse, self).__init__()
        self._dt = None
        self._user_owned_assets = None

    @property
    def dt(self):
        return self._dt

    @dt.setter
    def dt(self, value):
        self._dt = value
    @property
    def user_owned_assets(self):
        return self._user_owned_assets

    @user_owned_assets.setter
    def user_owned_assets(self, value):
        if isinstance(value, list):
            self._user_owned_assets = list()
            for i in value:
                if isinstance(i, UserOwnedAsset):
                    self._user_owned_assets.append(i)
                else:
                    self._user_owned_assets.append(UserOwnedAsset.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AnttechNftCtocUserassetQueryResponse, self).parse_response_content(response_content)
        if 'dt' in response:
            self.dt = response['dt']
        if 'user_owned_assets' in response:
            self.user_owned_assets = response['user_owned_assets']
