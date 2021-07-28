#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PortraitDistribution import PortraitDistribution


class AlipayOpenMiniUserportraitQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniUserportraitQueryResponse, self).__init__()
        self._portrait_distributions = None

    @property
    def portrait_distributions(self):
        return self._portrait_distributions

    @portrait_distributions.setter
    def portrait_distributions(self, value):
        if isinstance(value, list):
            self._portrait_distributions = list()
            for i in value:
                if isinstance(i, PortraitDistribution):
                    self._portrait_distributions.append(i)
                else:
                    self._portrait_distributions.append(PortraitDistribution.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniUserportraitQueryResponse, self).parse_response_content(response_content)
        if 'portrait_distributions' in response:
            self.portrait_distributions = response['portrait_distributions']
