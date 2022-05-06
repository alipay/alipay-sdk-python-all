#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFincoreComplianceApccenterAlgorithmarchiveDetectResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFincoreComplianceApccenterAlgorithmarchiveDetectResponse, self).__init__()
        self._can_skip = None
        self._disable_operation = None
        self._edit_url = None
        self._has_perfect = None
        self._platform_algorithm_code = None
        self._platform_algorithm_source = None
        self._remind_text = None
        self._view_url = None

    @property
    def can_skip(self):
        return self._can_skip

    @can_skip.setter
    def can_skip(self, value):
        self._can_skip = value
    @property
    def disable_operation(self):
        return self._disable_operation

    @disable_operation.setter
    def disable_operation(self, value):
        self._disable_operation = value
    @property
    def edit_url(self):
        return self._edit_url

    @edit_url.setter
    def edit_url(self, value):
        self._edit_url = value
    @property
    def has_perfect(self):
        return self._has_perfect

    @has_perfect.setter
    def has_perfect(self, value):
        self._has_perfect = value
    @property
    def platform_algorithm_code(self):
        return self._platform_algorithm_code

    @platform_algorithm_code.setter
    def platform_algorithm_code(self, value):
        self._platform_algorithm_code = value
    @property
    def platform_algorithm_source(self):
        return self._platform_algorithm_source

    @platform_algorithm_source.setter
    def platform_algorithm_source(self, value):
        self._platform_algorithm_source = value
    @property
    def remind_text(self):
        return self._remind_text

    @remind_text.setter
    def remind_text(self, value):
        self._remind_text = value
    @property
    def view_url(self):
        return self._view_url

    @view_url.setter
    def view_url(self, value):
        self._view_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayFincoreComplianceApccenterAlgorithmarchiveDetectResponse, self).parse_response_content(response_content)
        if 'can_skip' in response:
            self.can_skip = response['can_skip']
        if 'disable_operation' in response:
            self.disable_operation = response['disable_operation']
        if 'edit_url' in response:
            self.edit_url = response['edit_url']
        if 'has_perfect' in response:
            self.has_perfect = response['has_perfect']
        if 'platform_algorithm_code' in response:
            self.platform_algorithm_code = response['platform_algorithm_code']
        if 'platform_algorithm_source' in response:
            self.platform_algorithm_source = response['platform_algorithm_source']
        if 'remind_text' in response:
            self.remind_text = response['remind_text']
        if 'view_url' in response:
            self.view_url = response['view_url']
