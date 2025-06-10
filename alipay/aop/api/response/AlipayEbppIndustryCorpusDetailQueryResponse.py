#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DocDTO import DocDTO
from alipay.aop.api.domain.CommonQaDTO import CommonQaDTO
from alipay.aop.api.domain.ServiceItemDTO import ServiceItemDTO
from alipay.aop.api.domain.GovOrgServiceDTO import GovOrgServiceDTO


class AlipayEbppIndustryCorpusDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryCorpusDetailQueryResponse, self).__init__()
        self._doc_dto = None
        self._faq_dto = None
        self._item_dto = None
        self._service_dto = None

    @property
    def doc_dto(self):
        return self._doc_dto

    @doc_dto.setter
    def doc_dto(self, value):
        if isinstance(value, DocDTO):
            self._doc_dto = value
        else:
            self._doc_dto = DocDTO.from_alipay_dict(value)
    @property
    def faq_dto(self):
        return self._faq_dto

    @faq_dto.setter
    def faq_dto(self, value):
        if isinstance(value, CommonQaDTO):
            self._faq_dto = value
        else:
            self._faq_dto = CommonQaDTO.from_alipay_dict(value)
    @property
    def item_dto(self):
        return self._item_dto

    @item_dto.setter
    def item_dto(self, value):
        if isinstance(value, ServiceItemDTO):
            self._item_dto = value
        else:
            self._item_dto = ServiceItemDTO.from_alipay_dict(value)
    @property
    def service_dto(self):
        return self._service_dto

    @service_dto.setter
    def service_dto(self, value):
        if isinstance(value, GovOrgServiceDTO):
            self._service_dto = value
        else:
            self._service_dto = GovOrgServiceDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryCorpusDetailQueryResponse, self).parse_response_content(response_content)
        if 'doc_dto' in response:
            self.doc_dto = response['doc_dto']
        if 'faq_dto' in response:
            self.faq_dto = response['faq_dto']
        if 'item_dto' in response:
            self.item_dto = response['item_dto']
        if 'service_dto' in response:
            self.service_dto = response['service_dto']
