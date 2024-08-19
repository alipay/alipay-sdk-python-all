#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalAnttechAppcoreEnergysavingSubmitResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalAnttechAppcoreEnergysavingSubmitResponse, self).__init__()
        self._energy_saving_apply = None

    @property
    def energy_saving_apply(self):
        return self._energy_saving_apply

    @energy_saving_apply.setter
    def energy_saving_apply(self, value):
        self._energy_saving_apply = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalAnttechAppcoreEnergysavingSubmitResponse, self).parse_response_content(response_content)
        if 'energy_saving_apply' in response:
            self.energy_saving_apply = response['energy_saving_apply']
