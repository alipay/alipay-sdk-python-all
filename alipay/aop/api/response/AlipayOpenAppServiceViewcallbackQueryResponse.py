#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppServiceViewcallbackQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppServiceViewcallbackQueryResponse, self).__init__()
        self._catalog_map = None
        self._ext_info = None
        self._poi_ids = None
        self._service_carrier_code = None
        self._service_carrier_type = None
        self._service_carrier_url = None
        self._service_code = None
        self._service_granularity_type = None
        self._service_logo = None
        self._service_major_status = None
        self._service_name = None
        self._service_simple_desc = None
        self._service_spec_code = None

    @property
    def catalog_map(self):
        return self._catalog_map

    @catalog_map.setter
    def catalog_map(self, value):
        self._catalog_map = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def poi_ids(self):
        return self._poi_ids

    @poi_ids.setter
    def poi_ids(self, value):
        self._poi_ids = value
    @property
    def service_carrier_code(self):
        return self._service_carrier_code

    @service_carrier_code.setter
    def service_carrier_code(self, value):
        self._service_carrier_code = value
    @property
    def service_carrier_type(self):
        return self._service_carrier_type

    @service_carrier_type.setter
    def service_carrier_type(self, value):
        self._service_carrier_type = value
    @property
    def service_carrier_url(self):
        return self._service_carrier_url

    @service_carrier_url.setter
    def service_carrier_url(self, value):
        self._service_carrier_url = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def service_granularity_type(self):
        return self._service_granularity_type

    @service_granularity_type.setter
    def service_granularity_type(self, value):
        self._service_granularity_type = value
    @property
    def service_logo(self):
        return self._service_logo

    @service_logo.setter
    def service_logo(self, value):
        self._service_logo = value
    @property
    def service_major_status(self):
        return self._service_major_status

    @service_major_status.setter
    def service_major_status(self, value):
        self._service_major_status = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def service_simple_desc(self):
        return self._service_simple_desc

    @service_simple_desc.setter
    def service_simple_desc(self, value):
        self._service_simple_desc = value
    @property
    def service_spec_code(self):
        return self._service_spec_code

    @service_spec_code.setter
    def service_spec_code(self, value):
        self._service_spec_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppServiceViewcallbackQueryResponse, self).parse_response_content(response_content)
        if 'catalog_map' in response:
            self.catalog_map = response['catalog_map']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'poi_ids' in response:
            self.poi_ids = response['poi_ids']
        if 'service_carrier_code' in response:
            self.service_carrier_code = response['service_carrier_code']
        if 'service_carrier_type' in response:
            self.service_carrier_type = response['service_carrier_type']
        if 'service_carrier_url' in response:
            self.service_carrier_url = response['service_carrier_url']
        if 'service_code' in response:
            self.service_code = response['service_code']
        if 'service_granularity_type' in response:
            self.service_granularity_type = response['service_granularity_type']
        if 'service_logo' in response:
            self.service_logo = response['service_logo']
        if 'service_major_status' in response:
            self.service_major_status = response['service_major_status']
        if 'service_name' in response:
            self.service_name = response['service_name']
        if 'service_simple_desc' in response:
            self.service_simple_desc = response['service_simple_desc']
        if 'service_spec_code' in response:
            self.service_spec_code = response['service_spec_code']
