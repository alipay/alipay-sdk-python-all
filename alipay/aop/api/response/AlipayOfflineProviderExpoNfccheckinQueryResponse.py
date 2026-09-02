#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.NfcExpoCheckPlaceItemVO import NfcExpoCheckPlaceItemVO


class AlipayOfflineProviderExpoNfccheckinQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderExpoNfccheckinQueryResponse, self).__init__()
        self._activity_code = None
        self._activity_name = None
        self._nfc_expo_check_place_item_vos = None

    @property
    def activity_code(self):
        return self._activity_code

    @activity_code.setter
    def activity_code(self, value):
        self._activity_code = value
    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
    @property
    def nfc_expo_check_place_item_vos(self):
        return self._nfc_expo_check_place_item_vos

    @nfc_expo_check_place_item_vos.setter
    def nfc_expo_check_place_item_vos(self, value):
        if isinstance(value, list):
            self._nfc_expo_check_place_item_vos = list()
            for i in value:
                if isinstance(i, NfcExpoCheckPlaceItemVO):
                    self._nfc_expo_check_place_item_vos.append(i)
                else:
                    self._nfc_expo_check_place_item_vos.append(NfcExpoCheckPlaceItemVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderExpoNfccheckinQueryResponse, self).parse_response_content(response_content)
        if 'activity_code' in response:
            self.activity_code = response['activity_code']
        if 'activity_name' in response:
            self.activity_name = response['activity_name']
        if 'nfc_expo_check_place_item_vos' in response:
            self.nfc_expo_check_place_item_vos = response['nfc_expo_check_place_item_vos']
