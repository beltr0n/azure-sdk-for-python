# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._azure_monitor_exporter_enums import *


class MonitorDomain(msrest.serialization.Model):
    """The abstract common base of all domains.

    All required parameters must be populated in order to send to Azure.

    :param version: Required. Schema version.
    :type version: int
    """

    _validation = {
        'version': {'required': True},
    }

    _attribute_map = {
        'version': {'key': 'ver', 'type': 'int'},
    }

    def __init__(
        self,
        *,
        version: int = 2,
        **kwargs
    ):
        super(MonitorDomain, self).__init__(**kwargs)
        self.version = version


class AvailabilityData(MonitorDomain):
    """Instances of AvailabilityData represent the result of executing an availability test.

    All required parameters must be populated in order to send to Azure.

    :param version: Required. Schema version.
    :type version: int
    :param id: Required. Identifier of a test run. Use it to correlate steps of test run and
     telemetry generated by the service.
    :type id: str
    :param name: Required. Name of the test that these availability results represent.
    :type name: str
    :param duration: Required. Duration in format: DD.HH:MM:SS.MMMMMM. Must be less than 1000 days.
    :type duration: str
    :param success: Required. Success flag.
    :type success: bool
    :param run_location: Name of the location where the test was run from.
    :type run_location: str
    :param message: Diagnostic message for the result.
    :type message: str
    :param properties: Collection of custom properties.
    :type properties: dict[str, str]
    :param measurements: Collection of custom measurements.
    :type measurements: dict[str, float]
    """

    _validation = {
        'version': {'required': True},
        'id': {'required': True, 'max_length': 512, 'min_length': 0},
        'name': {'required': True, 'max_length': 1024, 'min_length': 0},
        'duration': {'required': True},
        'success': {'required': True},
        'run_location': {'max_length': 1024, 'min_length': 0},
        'message': {'max_length': 8192, 'min_length': 0},
    }

    _attribute_map = {
        'version': {'key': 'ver', 'type': 'int'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'duration': {'key': 'duration', 'type': 'str'},
        'success': {'key': 'success', 'type': 'bool'},
        'run_location': {'key': 'runLocation', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'measurements': {'key': 'measurements', 'type': '{float}'},
    }

    def __init__(
        self,
        *,
        version: int = 2,
        id: str,
        name: str,
        duration: str,
        success: bool,
        run_location: Optional[str] = None,
        message: Optional[str] = None,
        properties: Optional[Dict[str, str]] = None,
        measurements: Optional[Dict[str, float]] = None,
        **kwargs
    ):
        super(AvailabilityData, self).__init__(version=version, **kwargs)
        self.id = id
        self.name = name
        self.duration = duration
        self.success = success
        self.run_location = run_location
        self.message = message
        self.properties = properties
        self.measurements = measurements


class MessageData(MonitorDomain):
    """Instances of Message represent printf-like trace statements that are text-searched. Log4Net, NLog and other text-based log file entries are translated into instances of this type. The message does not have measurements.

    All required parameters must be populated in order to send to Azure.

    :param version: Required. Schema version.
    :type version: int
    :param message: Required. Trace message.
    :type message: str
    :param severity_level: Trace severity level. Possible values include: "Verbose", "Information",
     "Warning", "Error", "Critical".
    :type severity_level: str or ~azure_monitor_exporter.models.SeverityLevel
    :param properties: Collection of custom properties.
    :type properties: dict[str, str]
    :param measurements: Collection of custom measurements.
    :type measurements: dict[str, float]
    """

    _validation = {
        'version': {'required': True},
        'message': {'required': True, 'max_length': 32768, 'min_length': 0},
    }

    _attribute_map = {
        'version': {'key': 'ver', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
        'severity_level': {'key': 'severityLevel', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'measurements': {'key': 'measurements', 'type': '{float}'},
    }

    def __init__(
        self,
        *,
        version: int = 2,
        message: str,
        severity_level: Optional[Union[str, "SeverityLevel"]] = None,
        properties: Optional[Dict[str, str]] = None,
        measurements: Optional[Dict[str, float]] = None,
        **kwargs
    ):
        super(MessageData, self).__init__(version=version, **kwargs)
        self.message = message
        self.severity_level = severity_level
        self.properties = properties
        self.measurements = measurements


class MetricDataPoint(msrest.serialization.Model):
    """Metric data single measurement.

    All required parameters must be populated in order to send to Azure.

    :param namespace: Namespace of the metric.
    :type namespace: str
    :param name: Required. Name of the metric.
    :type name: str
    :param data_point_type: Metric type. Single measurement or the aggregated value. Possible
     values include: "Measurement", "Aggregation".
    :type data_point_type: str or ~azure_monitor_exporter.models.DataPointType
    :param value: Required. Single value for measurement. Sum of individual measurements for the
     aggregation.
    :type value: float
    :param count: Metric weight of the aggregated metric. Should not be set for a measurement.
    :type count: int
    :param min: Minimum value of the aggregated metric. Should not be set for a measurement.
    :type min: float
    :param max: Maximum value of the aggregated metric. Should not be set for a measurement.
    :type max: float
    :param std_dev: Standard deviation of the aggregated metric. Should not be set for a
     measurement.
    :type std_dev: float
    """

    _validation = {
        'namespace': {'max_length': 256, 'min_length': 0},
        'name': {'required': True, 'max_length': 1024, 'min_length': 0},
        'value': {'required': True},
    }

    _attribute_map = {
        'namespace': {'key': 'ns', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'data_point_type': {'key': 'kind', 'type': 'str'},
        'value': {'key': 'value', 'type': 'float'},
        'count': {'key': 'count', 'type': 'int'},
        'min': {'key': 'min', 'type': 'float'},
        'max': {'key': 'max', 'type': 'float'},
        'std_dev': {'key': 'stdDev', 'type': 'float'},
    }

    def __init__(
        self,
        *,
        name: str,
        value: float,
        namespace: Optional[str] = None,
        data_point_type: Optional[Union[str, "DataPointType"]] = None,
        count: Optional[int] = None,
        min: Optional[float] = None,
        max: Optional[float] = None,
        std_dev: Optional[float] = None,
        **kwargs
    ):
        super(MetricDataPoint, self).__init__(**kwargs)
        self.namespace = namespace
        self.name = name
        self.data_point_type = data_point_type
        self.value = value
        self.count = count
        self.min = min
        self.max = max
        self.std_dev = std_dev


class MetricsData(MonitorDomain):
    """An instance of the Metric item is a list of measurements (single data points) and/or aggregations.

    All required parameters must be populated in order to send to Azure.

    :param version: Required. Schema version.
    :type version: int
    :param metrics: Required. List of metrics. Only one metric in the list is currently supported
     by Application Insights storage. If multiple data points were sent only the first one will be
     used.
    :type metrics: list[~azure_monitor_exporter.models.MetricDataPoint]
    :param properties: Collection of custom properties.
    :type properties: dict[str, str]
    """

    _validation = {
        'version': {'required': True},
        'metrics': {'required': True},
    }

    _attribute_map = {
        'version': {'key': 'ver', 'type': 'int'},
        'metrics': {'key': 'metrics', 'type': '[MetricDataPoint]'},
        'properties': {'key': 'properties', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        version: int = 2,
        metrics: List["MetricDataPoint"],
        properties: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(MetricsData, self).__init__(version=version, **kwargs)
        self.metrics = metrics
        self.properties = properties


class MonitorBase(msrest.serialization.Model):
    """Data struct to contain only C section with custom fields.

    :param base_type: Name of item (B section) if any. If telemetry data is derived straight from
     this, this should be null.
    :type base_type: str
    :param base_data: The data payload for the telemetry request.
    :type base_data: ~azure_monitor_exporter.models.MonitorDomain
    """

    _attribute_map = {
        'base_type': {'key': 'baseType', 'type': 'str'},
        'base_data': {'key': 'baseData', 'type': 'MonitorDomain'},
    }

    def __init__(
        self,
        *,
        base_type: Optional[str] = None,
        base_data: Optional["MonitorDomain"] = None,
        **kwargs
    ):
        super(MonitorBase, self).__init__(**kwargs)
        self.base_type = base_type
        self.base_data = base_data


class PageViewData(MonitorDomain):
    """An instance of PageView represents a generic action on a page like a button click. It is also the base type for PageView.

    All required parameters must be populated in order to send to Azure.

    :param version: Required. Schema version.
    :type version: int
    :param id: Required. Identifier of a page view instance. Used for correlation between page view
     and other telemetry items.
    :type id: str
    :param name: Required. Event name. Keep it low cardinality to allow proper grouping and useful
     metrics.
    :type name: str
    :param url: Request URL with all query string parameters.
    :type url: str
    :param duration: Request duration in format: DD.HH:MM:SS.MMMMMM. For a page view
     (PageViewData), this is the duration. For a page view with performance information
     (PageViewPerfData), this is the page load time. Must be less than 1000 days.
    :type duration: str
    :param referred_uri: Fully qualified page URI or URL of the referring page; if unknown, leave
     blank.
    :type referred_uri: str
    :param properties: Collection of custom properties.
    :type properties: dict[str, str]
    :param measurements: Collection of custom measurements.
    :type measurements: dict[str, float]
    """

    _validation = {
        'version': {'required': True},
        'id': {'required': True, 'max_length': 512, 'min_length': 0},
        'name': {'required': True, 'max_length': 1024, 'min_length': 0},
        'url': {'max_length': 2048, 'min_length': 0},
        'referred_uri': {'max_length': 2048, 'min_length': 0},
    }

    _attribute_map = {
        'version': {'key': 'ver', 'type': 'int'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'duration': {'key': 'duration', 'type': 'str'},
        'referred_uri': {'key': 'referredUri', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'measurements': {'key': 'measurements', 'type': '{float}'},
    }

    def __init__(
        self,
        *,
        version: int = 2,
        id: str,
        name: str,
        url: Optional[str] = None,
        duration: Optional[str] = None,
        referred_uri: Optional[str] = None,
        properties: Optional[Dict[str, str]] = None,
        measurements: Optional[Dict[str, float]] = None,
        **kwargs
    ):
        super(PageViewData, self).__init__(version=version, **kwargs)
        self.id = id
        self.name = name
        self.url = url
        self.duration = duration
        self.referred_uri = referred_uri
        self.properties = properties
        self.measurements = measurements


class PageViewPerfData(MonitorDomain):
    """An instance of PageViewPerf represents: a page view with no performance data, a page view with performance data, or just the performance data of an earlier page request.

    All required parameters must be populated in order to send to Azure.

    :param version: Required. Schema version.
    :type version: int
    :param id: Required. Identifier of a page view instance. Used for correlation between page view
     and other telemetry items.
    :type id: str
    :param name: Required. Event name. Keep it low cardinality to allow proper grouping and useful
     metrics.
    :type name: str
    :param url: Request URL with all query string parameters.
    :type url: str
    :param duration: Request duration in format: DD.HH:MM:SS.MMMMMM. For a page view
     (PageViewData), this is the duration. For a page view with performance information
     (PageViewPerfData), this is the page load time. Must be less than 1000 days.
    :type duration: str
    :param perf_total: Performance total in TimeSpan 'G' (general long) format: d:hh:mm:ss.fffffff.
    :type perf_total: str
    :param network_connect: Network connection time in TimeSpan 'G' (general long) format:
     d:hh:mm:ss.fffffff.
    :type network_connect: str
    :param sent_request: Sent request time in TimeSpan 'G' (general long) format:
     d:hh:mm:ss.fffffff.
    :type sent_request: str
    :param received_response: Received response time in TimeSpan 'G' (general long) format:
     d:hh:mm:ss.fffffff.
    :type received_response: str
    :param dom_processing: DOM processing time in TimeSpan 'G' (general long) format:
     d:hh:mm:ss.fffffff.
    :type dom_processing: str
    :param properties: Collection of custom properties.
    :type properties: dict[str, str]
    :param measurements: Collection of custom measurements.
    :type measurements: dict[str, float]
    """

    _validation = {
        'version': {'required': True},
        'id': {'required': True, 'max_length': 512, 'min_length': 0},
        'name': {'required': True, 'max_length': 1024, 'min_length': 0},
        'url': {'max_length': 2048, 'min_length': 0},
    }

    _attribute_map = {
        'version': {'key': 'ver', 'type': 'int'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'duration': {'key': 'duration', 'type': 'str'},
        'perf_total': {'key': 'perfTotal', 'type': 'str'},
        'network_connect': {'key': 'networkConnect', 'type': 'str'},
        'sent_request': {'key': 'sentRequest', 'type': 'str'},
        'received_response': {'key': 'receivedResponse', 'type': 'str'},
        'dom_processing': {'key': 'domProcessing', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'measurements': {'key': 'measurements', 'type': '{float}'},
    }

    def __init__(
        self,
        *,
        version: int = 2,
        id: str,
        name: str,
        url: Optional[str] = None,
        duration: Optional[str] = None,
        perf_total: Optional[str] = None,
        network_connect: Optional[str] = None,
        sent_request: Optional[str] = None,
        received_response: Optional[str] = None,
        dom_processing: Optional[str] = None,
        properties: Optional[Dict[str, str]] = None,
        measurements: Optional[Dict[str, float]] = None,
        **kwargs
    ):
        super(PageViewPerfData, self).__init__(version=version, **kwargs)
        self.id = id
        self.name = name
        self.url = url
        self.duration = duration
        self.perf_total = perf_total
        self.network_connect = network_connect
        self.sent_request = sent_request
        self.received_response = received_response
        self.dom_processing = dom_processing
        self.properties = properties
        self.measurements = measurements


class RemoteDependencyData(MonitorDomain):
    """An instance of Remote Dependency represents an interaction of the monitored component with a remote component/service like SQL or an HTTP endpoint.

    All required parameters must be populated in order to send to Azure.

    :param version: Required. Schema version.
    :type version: int
    :param id: Identifier of a dependency call instance. Used for correlation with the request
     telemetry item corresponding to this dependency call.
    :type id: str
    :param name: Required. Name of the command initiated with this dependency call. Low cardinality
     value. Examples are stored procedure name and URL path template.
    :type name: str
    :param result_code: Result code of a dependency call. Examples are SQL error code and HTTP
     status code.
    :type result_code: str
    :param data: Command initiated by this dependency call. Examples are SQL statement and HTTP URL
     with all query parameters.
    :type data: str
    :param type: Dependency type name. Very low cardinality value for logical grouping of
     dependencies and interpretation of other fields like commandName and resultCode. Examples are
     SQL, Azure table, and HTTP.
    :type type: str
    :param target: Target site of a dependency call. Examples are server name, host address.
    :type target: str
    :param duration: Required. Request duration in format: DD.HH:MM:SS.MMMMMM. Must be less than
     1000 days.
    :type duration: str
    :param success: Indication of successful or unsuccessful call.
    :type success: bool
    :param properties: Collection of custom properties.
    :type properties: dict[str, str]
    :param measurements: Collection of custom measurements.
    :type measurements: dict[str, float]
    """

    _validation = {
        'version': {'required': True},
        'id': {'max_length': 512, 'min_length': 0},
        'name': {'required': True, 'max_length': 1024, 'min_length': 0},
        'result_code': {'max_length': 1024, 'min_length': 0},
        'data': {'max_length': 8192, 'min_length': 0},
        'type': {'max_length': 1024, 'min_length': 0},
        'target': {'max_length': 1024, 'min_length': 0},
        'duration': {'required': True},
    }

    _attribute_map = {
        'version': {'key': 'ver', 'type': 'int'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'result_code': {'key': 'resultCode', 'type': 'str'},
        'data': {'key': 'data', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'duration': {'key': 'duration', 'type': 'str'},
        'success': {'key': 'success', 'type': 'bool'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'measurements': {'key': 'measurements', 'type': '{float}'},
    }

    def __init__(
        self,
        *,
        version: int = 2,
        name: str,
        duration: str,
        id: Optional[str] = None,
        result_code: Optional[str] = None,
        data: Optional[str] = None,
        type: Optional[str] = None,
        target: Optional[str] = None,
        success: Optional[bool] = True,
        properties: Optional[Dict[str, str]] = None,
        measurements: Optional[Dict[str, float]] = None,
        **kwargs
    ):
        super(RemoteDependencyData, self).__init__(version=version, **kwargs)
        self.id = id
        self.name = name
        self.result_code = result_code
        self.data = data
        self.type = type
        self.target = target
        self.duration = duration
        self.success = success
        self.properties = properties
        self.measurements = measurements


class RequestData(MonitorDomain):
    """An instance of Request represents completion of an external request to the application to do work and contains a summary of that request execution and the results.

    All required parameters must be populated in order to send to Azure.

    :param version: Required. Schema version.
    :type version: int
    :param id: Required. Identifier of a request call instance. Used for correlation between
     request and other telemetry items.
    :type id: str
    :param name: Name of the request. Represents code path taken to process request. Low
     cardinality value to allow better grouping of requests. For HTTP requests it represents the
     HTTP method and URL path template like 'GET /values/{id}'.
    :type name: str
    :param duration: Required. Request duration in format: DD.HH:MM:SS.MMMMMM. Must be less than
     1000 days.
    :type duration: str
    :param success: Required. Indication of successful or unsuccessful call.
    :type success: bool
    :param response_code: Required. Result of a request execution. HTTP status code for HTTP
     requests.
    :type response_code: str
    :param source: Source of the request. Examples are the instrumentation key of the caller or the
     ip address of the caller.
    :type source: str
    :param url: Request URL with all query string parameters.
    :type url: str
    :param properties: Collection of custom properties.
    :type properties: dict[str, str]
    :param measurements: Collection of custom measurements.
    :type measurements: dict[str, float]
    """

    _validation = {
        'version': {'required': True},
        'id': {'required': True, 'max_length': 512, 'min_length': 0},
        'name': {'max_length': 1024, 'min_length': 0},
        'duration': {'required': True},
        'success': {'required': True},
        'response_code': {'required': True, 'max_length': 1024, 'min_length': 0},
        'source': {'max_length': 1024, 'min_length': 0},
        'url': {'max_length': 2048, 'min_length': 0},
    }

    _attribute_map = {
        'version': {'key': 'ver', 'type': 'int'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'duration': {'key': 'duration', 'type': 'str'},
        'success': {'key': 'success', 'type': 'bool'},
        'response_code': {'key': 'responseCode', 'type': 'str'},
        'source': {'key': 'source', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'measurements': {'key': 'measurements', 'type': '{float}'},
    }

    def __init__(
        self,
        *,
        version: int = 2,
        id: str,
        duration: str,
        success: bool = True,
        response_code: str,
        name: Optional[str] = None,
        source: Optional[str] = None,
        url: Optional[str] = None,
        properties: Optional[Dict[str, str]] = None,
        measurements: Optional[Dict[str, float]] = None,
        **kwargs
    ):
        super(RequestData, self).__init__(version=version, **kwargs)
        self.id = id
        self.name = name
        self.duration = duration
        self.success = success
        self.response_code = response_code
        self.source = source
        self.url = url
        self.properties = properties
        self.measurements = measurements


class StackFrame(msrest.serialization.Model):
    """Stack frame information.

    All required parameters must be populated in order to send to Azure.

    :param level: Required.
    :type level: int
    :param method: Required. Method name.
    :type method: str
    :param assembly: Name of the assembly (dll, jar, etc.) containing this function.
    :type assembly: str
    :param file_name: File name or URL of the method implementation.
    :type file_name: str
    :param line: Line number of the code implementation.
    :type line: int
    """

    _validation = {
        'level': {'required': True},
        'method': {'required': True, 'max_length': 1024, 'min_length': 0},
        'assembly': {'max_length': 1024, 'min_length': 0},
        'file_name': {'max_length': 1024, 'min_length': 0},
    }

    _attribute_map = {
        'level': {'key': 'level', 'type': 'int'},
        'method': {'key': 'method', 'type': 'str'},
        'assembly': {'key': 'assembly', 'type': 'str'},
        'file_name': {'key': 'fileName', 'type': 'str'},
        'line': {'key': 'line', 'type': 'int'},
    }

    def __init__(
        self,
        *,
        level: int,
        method: str,
        assembly: Optional[str] = None,
        file_name: Optional[str] = None,
        line: Optional[int] = None,
        **kwargs
    ):
        super(StackFrame, self).__init__(**kwargs)
        self.level = level
        self.method = method
        self.assembly = assembly
        self.file_name = file_name
        self.line = line


class TelemetryErrorDetails(msrest.serialization.Model):
    """The error details.

    :param index: The index in the original payload of the item.
    :type index: int
    :param status_code: The item specific `HTTP Response status code <#Response Status Codes>`_.
    :type status_code: int
    :param message: The error message.
    :type message: str
    """

    _attribute_map = {
        'index': {'key': 'index', 'type': 'int'},
        'status_code': {'key': 'statusCode', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        index: Optional[int] = None,
        status_code: Optional[int] = None,
        message: Optional[str] = None,
        **kwargs
    ):
        super(TelemetryErrorDetails, self).__init__(**kwargs)
        self.index = index
        self.status_code = status_code
        self.message = message


class TelemetryEventData(MonitorDomain):
    """Instances of Event represent structured event records that can be grouped and searched by their properties. Event data item also creates a metric of event count by name.

    All required parameters must be populated in order to send to Azure.

    :param version: Required. Schema version.
    :type version: int
    :param name: Required. Event name. Keep it low cardinality to allow proper grouping and useful
     metrics.
    :type name: str
    :param properties: Collection of custom properties.
    :type properties: dict[str, str]
    :param measurements: Collection of custom measurements.
    :type measurements: dict[str, float]
    """

    _validation = {
        'version': {'required': True},
        'name': {'required': True, 'max_length': 512, 'min_length': 0},
    }

    _attribute_map = {
        'version': {'key': 'ver', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'measurements': {'key': 'measurements', 'type': '{float}'},
    }

    def __init__(
        self,
        *,
        version: int = 2,
        name: str,
        properties: Optional[Dict[str, str]] = None,
        measurements: Optional[Dict[str, float]] = None,
        **kwargs
    ):
        super(TelemetryEventData, self).__init__(version=version, **kwargs)
        self.name = name
        self.properties = properties
        self.measurements = measurements


class TelemetryExceptionData(MonitorDomain):
    """An instance of Exception represents a handled or unhandled exception that occurred during execution of the monitored application.

    All required parameters must be populated in order to send to Azure.

    :param version: Required. Schema version.
    :type version: int
    :param exceptions: Required. Exception chain - list of inner exceptions.
    :type exceptions: list[~azure_monitor_exporter.models.TelemetryExceptionDetails]
    :param severity_level: Severity level. Mostly used to indicate exception severity level when it
     is reported by logging library. Possible values include: "Verbose", "Information", "Warning",
     "Error", "Critical".
    :type severity_level: str or ~azure_monitor_exporter.models.SeverityLevel
    :param problem_id: Identifier of where the exception was thrown in code. Used for exceptions
     grouping. Typically a combination of exception type and a function from the call stack.
    :type problem_id: str
    :param properties: Collection of custom properties.
    :type properties: dict[str, str]
    :param measurements: Collection of custom measurements.
    :type measurements: dict[str, float]
    """

    _validation = {
        'version': {'required': True},
        'exceptions': {'required': True},
        'problem_id': {'max_length': 1024, 'min_length': 0},
    }

    _attribute_map = {
        'version': {'key': 'ver', 'type': 'int'},
        'exceptions': {'key': 'exceptions', 'type': '[TelemetryExceptionDetails]'},
        'severity_level': {'key': 'severityLevel', 'type': 'str'},
        'problem_id': {'key': 'problemId', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'measurements': {'key': 'measurements', 'type': '{float}'},
    }

    def __init__(
        self,
        *,
        version: int = 2,
        exceptions: List["TelemetryExceptionDetails"],
        severity_level: Optional[Union[str, "SeverityLevel"]] = None,
        problem_id: Optional[str] = None,
        properties: Optional[Dict[str, str]] = None,
        measurements: Optional[Dict[str, float]] = None,
        **kwargs
    ):
        super(TelemetryExceptionData, self).__init__(version=version, **kwargs)
        self.exceptions = exceptions
        self.severity_level = severity_level
        self.problem_id = problem_id
        self.properties = properties
        self.measurements = measurements


class TelemetryExceptionDetails(msrest.serialization.Model):
    """Exception details of the exception in a chain.

    All required parameters must be populated in order to send to Azure.

    :param id: In case exception is nested (outer exception contains inner one), the id and outerId
     properties are used to represent the nesting.
    :type id: int
    :param outer_id: The value of outerId is a reference to an element in ExceptionDetails that
     represents the outer exception.
    :type outer_id: int
    :param type_name: Exception type name.
    :type type_name: str
    :param message: Required. Exception message.
    :type message: str
    :param has_full_stack: Indicates if full exception stack is provided in the exception. The
     stack may be trimmed, such as in the case of a StackOverflow exception.
    :type has_full_stack: bool
    :param stack: Text describing the stack. Either stack or parsedStack should have a value.
    :type stack: str
    :param parsed_stack: List of stack frames. Either stack or parsedStack should have a value.
    :type parsed_stack: list[~azure_monitor_exporter.models.StackFrame]
    """

    _validation = {
        'type_name': {'max_length': 1024, 'min_length': 0},
        'message': {'required': True, 'max_length': 32768, 'min_length': 0},
        'stack': {'max_length': 32768, 'min_length': 0},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'outer_id': {'key': 'outerId', 'type': 'int'},
        'type_name': {'key': 'typeName', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'has_full_stack': {'key': 'hasFullStack', 'type': 'bool'},
        'stack': {'key': 'stack', 'type': 'str'},
        'parsed_stack': {'key': 'parsedStack', 'type': '[StackFrame]'},
    }

    def __init__(
        self,
        *,
        message: str,
        id: Optional[int] = None,
        outer_id: Optional[int] = None,
        type_name: Optional[str] = None,
        has_full_stack: Optional[bool] = True,
        stack: Optional[str] = None,
        parsed_stack: Optional[List["StackFrame"]] = None,
        **kwargs
    ):
        super(TelemetryExceptionDetails, self).__init__(**kwargs)
        self.id = id
        self.outer_id = outer_id
        self.type_name = type_name
        self.message = message
        self.has_full_stack = has_full_stack
        self.stack = stack
        self.parsed_stack = parsed_stack


class TelemetryItem(msrest.serialization.Model):
    """System variables for a telemetry item.

    All required parameters must be populated in order to send to Azure.

    :param version: Envelope version. For internal use only. By assigning this the default, it will
     not be serialized within the payload unless changed to a value other than #1.
    :type version: int
    :param name: Required. Type name of telemetry data item.
    :type name: str
    :param time: Required. Event date time when telemetry item was created. This is the wall clock
     time on the client when the event was generated. There is no guarantee that the client's time
     is accurate. This field must be formatted in UTC ISO 8601 format, with a trailing 'Z'
     character, as described publicly on https://en.wikipedia.org/wiki/ISO_8601#UTC. Note: the
     number of decimal seconds digits provided are variable (and unspecified). Consumers should
     handle this, i.e. managed code consumers should not use format 'O' for parsing as it specifies
     a fixed length. Example: 2009-06-15T13:45:30.0000000Z.
    :type time: str
    :param sample_rate: Sampling rate used in application. This telemetry item represents 1 /
     sampleRate actual telemetry items.
    :type sample_rate: float
    :param sequence: Sequence field used to track absolute order of uploaded events.
    :type sequence: str
    :param instrumentation_key: The instrumentation key of the Application Insights resource.
    :type instrumentation_key: str
    :param tags: A set of tags. Key/value collection of context properties. See ContextTagKeys for
     information on available properties.
    :type tags: dict[str, str]
    :param data: Telemetry data item.
    :type data: ~azure_monitor_exporter.models.MonitorBase
    """

    _validation = {
        'name': {'required': True},
        'time': {'required': True},
        'sequence': {'max_length': 64, 'min_length': 0},
    }

    _attribute_map = {
        'version': {'key': 'ver', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'time': {'key': 'time', 'type': 'str'},
        'sample_rate': {'key': 'sampleRate', 'type': 'float'},
        'sequence': {'key': 'seq', 'type': 'str'},
        'instrumentation_key': {'key': 'iKey', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'data': {'key': 'data', 'type': 'MonitorBase'},
    }

    def __init__(
        self,
        *,
        name: str,
        time: str,
        version: Optional[int] = 1,
        sample_rate: Optional[float] = 100,
        sequence: Optional[str] = None,
        instrumentation_key: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        data: Optional["MonitorBase"] = None,
        **kwargs
    ):
        super(TelemetryItem, self).__init__(**kwargs)
        self.version = version
        self.name = name
        self.time = time
        self.sample_rate = sample_rate
        self.sequence = sequence
        self.instrumentation_key = instrumentation_key
        self.tags = tags
        self.data = data


class TrackResponse(msrest.serialization.Model):
    """Response containing the status of each telemetry item.

    :param items_received: The number of items received.
    :type items_received: int
    :param items_accepted: The number of items accepted.
    :type items_accepted: int
    :param errors: An array of error detail objects.
    :type errors: list[~azure_monitor_exporter.models.TelemetryErrorDetails]
    """

    _attribute_map = {
        'items_received': {'key': 'itemsReceived', 'type': 'int'},
        'items_accepted': {'key': 'itemsAccepted', 'type': 'int'},
        'errors': {'key': 'errors', 'type': '[TelemetryErrorDetails]'},
    }

    def __init__(
        self,
        *,
        items_received: Optional[int] = None,
        items_accepted: Optional[int] = None,
        errors: Optional[List["TelemetryErrorDetails"]] = None,
        **kwargs
    ):
        super(TrackResponse, self).__init__(**kwargs)
        self.items_received = items_received
        self.items_accepted = items_accepted
        self.errors = errors
