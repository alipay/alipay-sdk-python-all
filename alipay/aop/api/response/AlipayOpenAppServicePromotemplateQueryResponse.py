#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PromoAccessBaseCatalogVO import PromoAccessBaseCatalogVO
from alipay.aop.api.domain.PromoContentApiSchemaVO import PromoContentApiSchemaVO


class AlipayOpenAppServicePromotemplateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppServicePromotemplateQueryResponse, self).__init__()
        self._promo_access_catalog_vos = None
        self._promo_booth_desc = None
        self._promo_booth_desc_url = None
        self._promo_booth_entity_num_type = None
        self._promo_booth_entity_type = None
        self._promo_booth_id = None
        self._promo_booth_name = None
        self._promo_content_api_schema_vos = None

    @property
    def promo_access_catalog_vos(self):
        return self._promo_access_catalog_vos

    @promo_access_catalog_vos.setter
    def promo_access_catalog_vos(self, value):
        if isinstance(value, list):
            self._promo_access_catalog_vos = list()
            for i in value:
                if isinstance(i, PromoAccessBaseCatalogVO):
                    self._promo_access_catalog_vos.append(i)
                else:
                    self._promo_access_catalog_vos.append(PromoAccessBaseCatalogVO.from_alipay_dict(i))
    @property
    def promo_booth_desc(self):
        return self._promo_booth_desc

    @promo_booth_desc.setter
    def promo_booth_desc(self, value):
        self._promo_booth_desc = value
    @property
    def promo_booth_desc_url(self):
        return self._promo_booth_desc_url

    @promo_booth_desc_url.setter
    def promo_booth_desc_url(self, value):
        self._promo_booth_desc_url = value
    @property
    def promo_booth_entity_num_type(self):
        return self._promo_booth_entity_num_type

    @promo_booth_entity_num_type.setter
    def promo_booth_entity_num_type(self, value):
        self._promo_booth_entity_num_type = value
    @property
    def promo_booth_entity_type(self):
        return self._promo_booth_entity_type

    @promo_booth_entity_type.setter
    def promo_booth_entity_type(self, value):
        self._promo_booth_entity_type = value
    @property
    def promo_booth_id(self):
        return self._promo_booth_id

    @promo_booth_id.setter
    def promo_booth_id(self, value):
        self._promo_booth_id = value
    @property
    def promo_booth_name(self):
        return self._promo_booth_name

    @promo_booth_name.setter
    def promo_booth_name(self, value):
        self._promo_booth_name = value
    @property
    def promo_content_api_schema_vos(self):
        return self._promo_content_api_schema_vos

    @promo_content_api_schema_vos.setter
    def promo_content_api_schema_vos(self, value):
        if isinstance(value, list):
            self._promo_content_api_schema_vos = list()
            for i in value:
                if isinstance(i, PromoContentApiSchemaVO):
                    self._promo_content_api_schema_vos.append(i)
                else:
                    self._promo_content_api_schema_vos.append(PromoContentApiSchemaVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppServicePromotemplateQueryResponse, self).parse_response_content(response_content)
        if 'promo_access_catalog_vos' in response:
            self.promo_access_catalog_vos = response['promo_access_catalog_vos']
        if 'promo_booth_desc' in response:
            self.promo_booth_desc = response['promo_booth_desc']
        if 'promo_booth_desc_url' in response:
            self.promo_booth_desc_url = response['promo_booth_desc_url']
        if 'promo_booth_entity_num_type' in response:
            self.promo_booth_entity_num_type = response['promo_booth_entity_num_type']
        if 'promo_booth_entity_type' in response:
            self.promo_booth_entity_type = response['promo_booth_entity_type']
        if 'promo_booth_id' in response:
            self.promo_booth_id = response['promo_booth_id']
        if 'promo_booth_name' in response:
            self.promo_booth_name = response['promo_booth_name']
        if 'promo_content_api_schema_vos' in response:
            self.promo_content_api_schema_vos = response['promo_content_api_schema_vos']
