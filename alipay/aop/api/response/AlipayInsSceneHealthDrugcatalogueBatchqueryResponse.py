#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HealthDrugCatalogueItem import HealthDrugCatalogueItem


class AlipayInsSceneHealthDrugcatalogueBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneHealthDrugcatalogueBatchqueryResponse, self).__init__()
        self._drug_item_list = None

    @property
    def drug_item_list(self):
        return self._drug_item_list

    @drug_item_list.setter
    def drug_item_list(self, value):
        if isinstance(value, list):
            self._drug_item_list = list()
            for i in value:
                if isinstance(i, HealthDrugCatalogueItem):
                    self._drug_item_list.append(i)
                else:
                    self._drug_item_list.append(HealthDrugCatalogueItem.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneHealthDrugcatalogueBatchqueryResponse, self).parse_response_content(response_content)
        if 'drug_item_list' in response:
            self.drug_item_list = response['drug_item_list']
