#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IntelligentPromo import IntelligentPromo
from alipay.aop.api.domain.PromoPageResult import PromoPageResult


class KoubeiMarketingCampaignIntelligentPromoBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignIntelligentPromoBatchqueryResponse, self).__init__()
        self._intelligent_promos = None
        self._page_result = None

    @property
    def intelligent_promos(self):
        return self._intelligent_promos

    @intelligent_promos.setter
    def intelligent_promos(self, value):
        if isinstance(value, list):
            self._intelligent_promos = list()
            for i in value:
                if isinstance(i, IntelligentPromo):
                    self._intelligent_promos.append(i)
                else:
                    self._intelligent_promos.append(IntelligentPromo.from_alipay_dict(i))
    @property
    def page_result(self):
        return self._page_result

    @page_result.setter
    def page_result(self, value):
        if isinstance(value, PromoPageResult):
            self._page_result = value
        else:
            self._page_result = PromoPageResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignIntelligentPromoBatchqueryResponse, self).parse_response_content(response_content)
        if 'intelligent_promos' in response:
            self.intelligent_promos = response['intelligent_promos']
        if 'page_result' in response:
            self.page_result = response['page_result']
