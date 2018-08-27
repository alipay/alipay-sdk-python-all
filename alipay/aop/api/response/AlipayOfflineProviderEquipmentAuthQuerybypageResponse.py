#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EquipmentAuthRemoveQueryBypageDTO import EquipmentAuthRemoveQueryBypageDTO


class AlipayOfflineProviderEquipmentAuthQuerybypageResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderEquipmentAuthQuerybypageResponse, self).__init__()
        self._equipmentauthremovequerybypagelist = None
        self._total = None

    @property
    def equipmentauthremovequerybypagelist(self):
        return self._equipmentauthremovequerybypagelist

    @equipmentauthremovequerybypagelist.setter
    def equipmentauthremovequerybypagelist(self, value):
        if isinstance(value, list):
            self._equipmentauthremovequerybypagelist = list()
            for i in value:
                if isinstance(i, EquipmentAuthRemoveQueryBypageDTO):
                    self._equipmentauthremovequerybypagelist.append(i)
                else:
                    self._equipmentauthremovequerybypagelist.append(EquipmentAuthRemoveQueryBypageDTO.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderEquipmentAuthQuerybypageResponse, self).parse_response_content(response_content)
        if 'equipmentauthremovequerybypagelist' in response:
            self.equipmentauthremovequerybypagelist = response['equipmentauthremovequerybypagelist']
        if 'total' in response:
            self.total = response['total']
