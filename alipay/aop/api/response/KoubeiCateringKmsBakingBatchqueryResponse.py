#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KmsBakingSalesForecastDTO import KmsBakingSalesForecastDTO


class KoubeiCateringKmsBakingBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringKmsBakingBatchqueryResponse, self).__init__()
        self._baking_sales_forecast_data = None

    @property
    def baking_sales_forecast_data(self):
        return self._baking_sales_forecast_data

    @baking_sales_forecast_data.setter
    def baking_sales_forecast_data(self, value):
        if isinstance(value, list):
            self._baking_sales_forecast_data = list()
            for i in value:
                if isinstance(i, KmsBakingSalesForecastDTO):
                    self._baking_sales_forecast_data.append(i)
                else:
                    self._baking_sales_forecast_data.append(KmsBakingSalesForecastDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringKmsBakingBatchqueryResponse, self).parse_response_content(response_content)
        if 'baking_sales_forecast_data' in response:
            self.baking_sales_forecast_data = response['baking_sales_forecast_data']
