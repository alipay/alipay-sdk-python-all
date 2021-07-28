#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialAntforestPlantConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialAntforestPlantConsultResponse, self).__init__()
        self._current_energy = None
        self._project_alliable = None

    @property
    def current_energy(self):
        return self._current_energy

    @current_energy.setter
    def current_energy(self, value):
        self._current_energy = value
    @property
    def project_alliable(self):
        return self._project_alliable

    @project_alliable.setter
    def project_alliable(self, value):
        self._project_alliable = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialAntforestPlantConsultResponse, self).parse_response_content(response_content)
        if 'current_energy' in response:
            self.current_energy = response['current_energy']
        if 'project_alliable' in response:
            self.project_alliable = response['project_alliable']
