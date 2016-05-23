# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.16.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::Network
  module Models
    #
    # Properties of ExpressRouteServiceProvider
    #
    class ExpressRouteServiceProviderPropertiesFormat

      include MsRestAzure

      # @return [Array<String>] Gets or list of peering locations
      attr_accessor :peering_locations

      # @return [Array<ExpressRouteServiceProviderBandwidthsOffered>] Gets or
      # bandwidths offered
      attr_accessor :bandwidths_offered

      # @return [String] Gets or sets Provisioning state of the resource
      attr_accessor :provisioning_state

      #
      # Validate the object. Throws ValidationError if validation fails.
      #
      def validate
        @peering_locations.each{ |e| e.validate if e.respond_to?(:validate) } unless @peering_locations.nil?
        @bandwidths_offered.each{ |e| e.validate if e.respond_to?(:validate) } unless @bandwidths_offered.nil?
      end

      #
      # Serializes given Model object into Ruby Hash.
      # @param object Model object to serialize.
      # @return [Hash] Serialized object in form of Ruby Hash.
      #
      def self.serialize_object(object)
        object.validate
        output_object = {}

        serialized_property = object.peering_locations
        output_object['peeringLocations'] = serialized_property unless serialized_property.nil?

        serialized_property = object.bandwidths_offered
        unless serialized_property.nil?
          serializedArray = []
          serialized_property.each do |element1|
            unless element1.nil?
              element1 = ExpressRouteServiceProviderBandwidthsOffered.serialize_object(element1)
            end
            serializedArray.push(element1)
          end
          serialized_property = serializedArray
        end
        output_object['bandwidthsOffered'] = serialized_property unless serialized_property.nil?

        serialized_property = object.provisioning_state
        output_object['provisioningState'] = serialized_property unless serialized_property.nil?

        output_object
      end

      #
      # Deserializes given Ruby Hash into Model object.
      # @param object [Hash] Ruby Hash object to deserialize.
      # @return [ExpressRouteServiceProviderPropertiesFormat] Deserialized
      # object.
      #
      def self.deserialize_object(object)
        return if object.nil?
        output_object = ExpressRouteServiceProviderPropertiesFormat.new

        deserialized_property = object['peeringLocations']
        output_object.peering_locations = deserialized_property

        deserialized_property = object['bandwidthsOffered']
        unless deserialized_property.nil?
          deserialized_array = []
          deserialized_property.each do |element3|
            unless element3.nil?
              element3 = ExpressRouteServiceProviderBandwidthsOffered.deserialize_object(element3)
            end
            deserialized_array.push(element3)
          end
          deserialized_property = deserialized_array
        end
        output_object.bandwidths_offered = deserialized_property

        deserialized_property = object['provisioningState']
        output_object.provisioning_state = deserialized_property

        output_object
      end
    end
  end
end