#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeliveryDetailPositionVO import DeliveryDetailPositionVO
from alipay.aop.api.domain.DeliveryDetailPositionPipelineConfigVO import DeliveryDetailPositionPipelineConfigVO


class AntfortuneStockCustomerDeliverydetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneStockCustomerDeliverydetailQueryResponse, self).__init__()
        self._agreement_no = None
        self._delivery_detail_position = None
        self._delivery_detail_position_pipeline_config = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def delivery_detail_position(self):
        return self._delivery_detail_position

    @delivery_detail_position.setter
    def delivery_detail_position(self, value):
        if isinstance(value, DeliveryDetailPositionVO):
            self._delivery_detail_position = value
        else:
            self._delivery_detail_position = DeliveryDetailPositionVO.from_alipay_dict(value)
    @property
    def delivery_detail_position_pipeline_config(self):
        return self._delivery_detail_position_pipeline_config

    @delivery_detail_position_pipeline_config.setter
    def delivery_detail_position_pipeline_config(self, value):
        if isinstance(value, list):
            self._delivery_detail_position_pipeline_config = list()
            for i in value:
                if isinstance(i, DeliveryDetailPositionPipelineConfigVO):
                    self._delivery_detail_position_pipeline_config.append(i)
                else:
                    self._delivery_detail_position_pipeline_config.append(DeliveryDetailPositionPipelineConfigVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AntfortuneStockCustomerDeliverydetailQueryResponse, self).parse_response_content(response_content)
        if 'agreement_no' in response:
            self.agreement_no = response['agreement_no']
        if 'delivery_detail_position' in response:
            self.delivery_detail_position = response['delivery_detail_position']
        if 'delivery_detail_position_pipeline_config' in response:
            self.delivery_detail_position_pipeline_config = response['delivery_detail_position_pipeline_config']
