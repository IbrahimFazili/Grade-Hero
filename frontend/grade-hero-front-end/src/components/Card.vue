<template>
    <v-card
      class="mx-auto elevation-10"
      :color= cardColour
      theme="dark"
      max-width="200"
    >
    <!-- <template v-slot:prepend>
    <v-icon size="x-large"></v-icon>
    </template> -->

    <v-card-text class="text-h5">
        {{ name }}
    </v-card-text>

    <!-- <v-card-actions>
    <v-list-item class="w-100">
        <template v-slot:prepend>
        <v-avatar
            color="grey-darken-3"
            image="https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light"
        ></v-avatar>
        </template>

        <v-list-item-title>Evan You</v-list-item-title>

        <v-list-item-subtitle>Vue Creator</v-list-item-subtitle>

        <template v-slot:append>
        <div class="justify-self-end">
            <v-icon class="me-1" icon="mdi-heart"></v-icon>
            <span class="subheading me-2">256</span>
            <span class="me-1">·</span>
            <v-icon class="me-1" icon="mdi-share-variant"></v-icon>
            <span class="subheading">45</span>
        </div>
        </template>
    </v-list-item>
    </v-card-actions> -->
    </v-card>
</template>

<script lang="ts">
import { onMounted } from 'vue';


    export default {
        props: {
            name: {
                type: String,
                required: true
            },
            cardColour: {
                type: String,
                required: true
            }
        },
    }

</script>