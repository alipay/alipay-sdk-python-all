#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CraftsmanWorkOutIdOpenModel import CraftsmanWorkOutIdOpenModel


class KoubeiCraftsmanDataWorkCreateResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCraftsmanDataWorkCreateResponse, self).__init__()
        self._works = None

    @property
    def works(self):
        return self._works

    @works.setter
    def works(self, value):
        if isinstance(value, list):
            self._works = list()
            for i in value:
                if isinstance(i, CraftsmanWorkOutIdOpenModel):
                    self._works.append(i)
                else:
                    self._works.append(CraftsmanWorkOutIdOpenModel.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiCraftsmanDataWorkCreateResponse, self).parse_response_content(response_content)
        if 'works' in response:
            self.works = response['works']
